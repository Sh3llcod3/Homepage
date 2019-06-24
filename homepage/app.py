#!/usr/bin/env python3
# Import required modules

from __future__ import unicode_literals

from flask import Flask, render_template, request

import youtube_dl

# Setup our Video class, this will handle the youtube_dl side of things.
class Video():

    # Initialise the class.
    def __init__(self, video_link):
        self.video_link = video_link
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': './downloads/%(title)s.%(ext)s'
        }

    # Add our download() method to download the video.
    def download(self):
        with youtube_dl.YoutubeDL(self.ydl_opts) as self.ydl:
            self.ydl.download([self.video_link])


app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["GET", "POST"])
def index_page():
    if request.method == "GET":
        with open("./templates/site.html", "r") as site:
            return site.read()
        #return render_template("./site.html")

    if request.method == "POST":
        # dl_request = Video(request.form["videoURL"])
        #dl_request.download()
        # kek = [request.form["videoURL"], request.form["radio_1"], request.form["radio_2"], request.form["attach_thumb"]]
        print(request.form)
        return request.form["radio_1"]


def main():
    app.run(host='0.0.0.0', port=5000)  # noqa: S104


if __name__ == "__main__":
    main()
