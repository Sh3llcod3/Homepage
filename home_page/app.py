#!/usr/bin/env python3
from __future__ import unicode_literals

from flask import Flask, render_template, request

import youtube_dl


class Video():
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

    def download(self):
        with youtube_dl.YoutubeDL(self.ydl_opts) as self.ydl:
            self.ydl.download([self.video_link])


app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["GET", "POST"])
def index_page():
    if request.method == "GET":
        return render_template("./site.html")

    if request.method == "POST":
        dl_request = Video(request.form["videoURL"])
        dl_request.download()
        return request.form["videoURL"]


def main():
    app.run(host='0.0.0.0', port=5000)  # noqa: S104


if __name__ == "__main__":
    main()
