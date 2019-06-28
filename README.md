# HomePage

HomePage is a trivial flask web app that allows downloading the audio track from almost any internet video.
It is intended to be deployed inside a private network for personal use, so that hosts within the network can access
and download the tracks they want.

HomePage is very basic, but it has a Material Design front-end which is simple and easy to use.
HomePage uses `youtube_dl` to download the videos, so quite a few sites are supported.

![HomePage](homepage/static/HomePage.png)

## Setup & Prerequsites

- The `apt` package manager
- `python3.6` or above
- The `pip` module for the above python version
- `sudo` access if you wish to use port `80`
- A Debian based distro. (tested on: Ubuntu 18.04 LTS)
- `pyenv` installed (optional)
- `poetry` installed (optional)

The basic installation is very simple.

```bash
$ python3 -m pip install homepage
$ homepage -ip
```

Then, you can deploy with:

```bash
$ homepage -df
```

Alternatively, if your system is running an older version of python or you wish to run this project inside
a virtual environment, you can do that too. In fact, this is the __recommended__ method of installing this project.

First, go ahead and install [pyenv](https://github.com/pyenv/pyenv#basic-github-checkout). Then install [poetry](https://github.com/sdispater/poetry).
Once you've installed those, we just to install a few more things.

```bash
$ git clone https://github.com/Sh3llcod3/HomePage.git
$ cd HomePage/
$ pyenv install 3.7.3
$ pyenv local 3.7.3
$ poetry self:update --preview || poetry self update --preview
$ poetry update
$ poetry install
$ poetry shell
$ homepage -ip
$ homepage -df
```

After installing `pyenv`, the lines you add to your `~/.bashrc` may need to be different, please see the [FAQ](#faq-&-troubleshooting).

## Usage

Once deployed, if you're using this on the device which is hosting it, fire up your
favourite web browser and head to `http://0.0.0.0:5000/`. If you're on another device,
simply head to the IP address that it prints out when you run it.

If you have `sudo` access, please use the `-f` switch. If you don't, other hosts can
still use this, but they will need to explicitly specify the port, e.g. `http://192.168.0.10:5000`.

From there, you just need to select your options and paste in a link to the video or playlist
that you want to download the tracks from. Obviously, you can download from `YouTube`, but thanks
to the power of the `youtube_dl` library, many other sites will also work, e.g. `Vimeo`, or `Reddit`.
You can find the full list [here](https://bit.ly/2XKgkuV).

## FAQ & Troubleshooting

#### I'm having trouble with the env

You may have inserted the wrong lines in your `~/.bashrc`.
The initialization lines shown on the pyenv repo don't work
well with poetry. Instead, add these lines to the end of the file
and remove any previous lines you may have added before
(taking care to ensure you don't remove anything else).

```bash
# Pyenv installation

if [[ -z "$VIRTUAL_ENV" ]]; then
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
fi
```

#### Can I change the background?

You absolutely can. To change the background, change out `homepage/static/Background.jpg` with any image you like,
but it has to be called `Background.jpg` and in the `JPEG` format. I will make this process easier in the future.

#### Pyenv fails to install 3.7.3

You may have forgotten to install some crucial `pyenv` dependencies from `apt`.
Go ahead and install the packages below. If you're using other package managers,
`HomePage` won't work, but [here](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) is their wiki page.

```bash
$ sudo apt update
$ sudo apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

#### Why does HomePage exist?

That is a really good question.
I wanted a simple web app where I could download music from various videos on any
device, without having access to a command line version of `youtube_dl` or resorting
to using shady sites and apps.

The code is bad at best, but it is functional and you have the freedom of choice.
Whether you want to use it or not is up to you, but I assumed that people prefer
convenience, so I should probably upload this where more people may be able to take
advantage of this.

#### Does HomePage scale?

No. It was never intended to scale in the first place. Neither is it secure in any way.
Therefore, I should stress that you should __NOT__ deploy this to anywhere except your
private/internal network.

#### Why does it take a long time?

Time is of the essence. I understand that if a specific computational task does not complete
as quickly as someone anticipates, it can leave the user feeling disappointed.

However, the length of time it takes for a specific video to be downloaded heavily depends
on several factors, such as the length, quantity and chosen quality of the download.
On top of this, you have to consider that for each video you download, `youtube_dl` has
to first download the video, then it has to be encoded in your preferred format using
`ffmpeg`. That can take a while, especially on older systems.

I am always looking to optimise this so it downloads and converts the videos faster, but
if you have any tips, please create an issue and I'll check it out as soon as possible.

## To-do

- [ ] Add an authentication page.
- [ ] Make site restore state after a download.
- [ ] Save user preferences using cookies.
- [ ] Display past tracks only for that host.
- [ ] Add a separate page for management.
