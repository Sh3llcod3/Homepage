#!/usr/bin/env python3

# Import required modules
from __future__ import unicode_literals

from atexit import register
from base64 import b64encode
from datetime import datetime
from os import walk
from shutil import make_archive
from subprocess import call, check_output  # noqa: S404
from sys import argv, exit

import easyparse

from flask import Flask, jsonify, render_template, request

import youtube_dl

version_string = " * HomePage, v0.1.0\n * Copyright (c) 2019 Yudhajit N. (MIT License)"


# Setup our Video class, this will handle the youtube_dl side of things.
class Video():

    # Initialise the class.
    def __init__(self, post_request):
        self.post_request = post_request
        self.video_link = post_request["videoURL"]
        self.mime_type = post_request["format_preference"]
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': f'{self.mime_type}',
                'preferredquality': '192',
            }],
            'outtmpl': './downloaded_tracks/%(title)s.%(ext)s'
        }
        if post_request["attach_thumb"].lower() == "yes":
            self.ydl_opts["writethumbnail"] = True
            self.ydl_opts["postprocessors"].append({'key': 'EmbedThumbnail', })
        if self.mime_type == "m4a":
            self.ydl_opts['postprocessor_args'] = [
                '-strict', '-2'
            ]

    # Add our download() method to download the video.
    def download(self):
        with youtube_dl.YoutubeDL(self.ydl_opts) as self.ydl:
            self.ydl.download([self.video_link])

    # Add our send_files() method to handle transfer.
    def send_files(self):
        path, dirs, files = next(walk("./downloaded_tracks/"))
        file_count = len(files)
        self.final_file_name = str()
        self.final_file_location = str()

        # The link is invalid
        if file_count == 0:
            with open("./templates/error_template.html", "r") as error:
                return error.read()

        # We have more than one file, so let's zip them up and send them back.
        if file_count > 1:
            self.final_file_name = "tracks_" + str(datetime.now().timestamp()).replace('.', '')
            self.final_file_location = "/tmp/" + self.final_file_name  # noqa: S108
            make_archive(self.final_file_location, 'zip', "downloaded_tracks")
            self.final_file_name += ".zip"
            self.final_file_location += ".zip"
            self.mime_type = "application/zip"

        # We only have one track, so let's send the file back.
        else:
            self.final_file_name = check_output("ls ./downloaded_tracks/",  # noqa: S607
                                                  shell=True).decode("utf-8").rstrip()  # noqa: S602
            self.final_file_location = "./downloaded_tracks/" + self.final_file_name

        with open(self.final_file_location, "rb") as file_to_send:
            file_to_send = b64encode(file_to_send.read()).decode()

        call("cp ./downloaded_tracks/* ./downloads/", shell=True)  # noqa: S607, S602
        call("rm ./downloaded_tracks/*", shell=True)  # noqa: S607, S602
        call(f"rm /tmp/tracks_* 2>/dev/null", shell=True)  # noqa: S607, S602
        return file_to_send


app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["GET", "POST"])
def index_page():
    if request.method == "GET":
        # with open("./templates/site.html", "r") as site:
        #    return site.read()
        return render_template("./site.html")

    if request.method == "POST":
        dl_request = Video(request.form)
        dl_request.download()
        file_bytes = dl_request.send_files()
        return jsonify({
            "file_name": dl_request.final_file_name,
            "file_contents": file_bytes,
            "format": f"audio/{dl_request.mime_type}"
        })


def main():

    # Setup our argument parser
    parser = easyparse.opt_parser(argv)
    parser.add_comment("Deploy for the first time: homepage -fdip")
    parser.add_comment("Deploy the app normally: homepage -df")
    parser.add_comment("I am aware it complains about using a WSGI server.")
    parser.add_comment("This app isn't designed to scale at all, on purpose.")
    parser.add_comment("Please don't deploy this outside your internal network.")
    parser.add_arg(
        "-h",
        "--help",
        None,
        "Show this help screen and exit.",
        optional=True
    )
    parser.add_arg(
        "-v",
        "--version",
        None,
        "Print version information and exit.",
        optional=True
    )
    parser.add_arg(
        "-d",
        "--deploy-app",
        None,
        "Deploy the app and start the flask server.",
        optional=False
    )
    parser.add_arg(
        "-f",
        "--forward-to-all-hosts",
        None,
        "Add an iptables rule forwarding port 80 to 5000 for convenience.",
        optional=False
    )
    parser.add_arg(
        "-p",
        "--purge-cache",
        None,
        "If supplied, remove all past downloaded tracks.",
        optional=False
    )
    parser.add_arg(
        "-i",
        "--install-dependencies",
        None,
        "Install some apt dependencies, only need to run once.",
        optional=False
    )
    parser.parse_args()

    # View the help screen
    if parser.is_present("-h") or len(argv) == 1:
        parser.filename = "homepage"
        parser.show_help()
        exit()

    # Print the version.
    if parser.is_present("-v"):
        print(version_string)
        exit()

    # Add the iptables rule
    def remove_rule():
        print("\n * Reverting iptables rule.")
        call(("sudo iptables -t nat -D PREROUTING -i enp2s0 "  # noqa: S607
              "-p tcp --dport 80 -j REDIRECT --to-port 5000"), shell=True)  # noqa: S602

    if parser.is_present("-f"):
        print(" * Adding iptables rule.")
        call(("sudo iptables -t nat -A PREROUTING -i enp2s0 "  # noqa: S607
              "-p tcp --dport 80 -j REDIRECT --to-port 5000"), shell=True)  # noqa: S602
        register(remove_rule)

    # Delete the previous downloaded tracks
    if parser.is_present("-p"):
        print(" * Purging downloaded tracks.")
        call("rm ./downloaded_tracks/* ./downloads/* 2>/dev/null", shell=True)  # noqa: S602, S607

    # Install the apt dependencies.
    if parser.is_present("-i"):
        call("sudo apt update && sudo apt install ffmpeg lame atomicparsley faac libav-tools -y",  # noqa: S607
              shell=True)  # noqa: S602

    # Run the app
    if parser.is_present("-d"):
        app.run(host='0.0.0.0', port=5000)  # noqa: S104


if __name__ == "__main__":
    main()
