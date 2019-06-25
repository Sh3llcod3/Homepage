# HomePage

HomePage is a simple flask webapp that allows downloading the audio track from almost any internet video.
It is intended to be deployed inside a private network, and hosts within the network can access
and download the tracks they want. HomePage's stand-out features are its Material Design interface
and simplicity. HomePage uses `youtube_dl` to download the videos, so quite a few sites are supported.

## Setup & Prerequsites

HomePage should be deployable on almost any Debian-like system that uses the `apt` package manager.
There are multiple ways to install and deploy the webapp, but the simplest way, is to just install
it direct from PyPi, assuming `python3.6` or above is present on the system.

```
python3 -m pip install homepage
homepage -i
homepage -fdp
```

Alternatively, you could also clone it from GitHub.

```
git clone https://github.com/Sh3llcod3/HomePage.git
cd HomePage/
python3 -m pip install -r requirements.txt
cd homepage/
./homepage.py -i
./homepage.py -fdp
```

## Usage



## FAQ & Troubleshooting



## To-do
