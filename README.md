# HomePage

HomePage is a trivial flask web app that allows downloading the audio track from almost any internet video.
It is intended to be deployed inside a private network for personal use, so that hosts within the network can access
and download the tracks they want.

HomePage is very basic, but it has a Material Design front-end which is simple and easy to use.
HomePage uses `youtube_dl` to download the videos, so quite a few sites are supported. Playlists are also supported.

![HomePage](homepage/static/HomePage.png)

## Setup & Prerequsites

- `python 3.6` or above
- The `pip` module for the above python version
- `sudo` access
- `pyenv` installed (optional)
- `poetry` installed (optional)

The basic installation is very simple.

```bash
$ python3 -m pip install --user homepage

# Normal desktop
$ homepage -i

# TTY only server
$ homepage -ic
```

Then, you can deploy with:

```bash
$ homepage -df
```

Alternatively, if your system is running an older version of python or you wish to run this project inside
a virtual environment, you can do that too.

First, go ahead and install [pyenv](https://github.com/pyenv/pyenv#basic-github-checkout). Then install [poetry](https://github.com/sdispater/poetry).
Once you've installed those, we just to install a few more things.

```bash
$ git clone https://github.com/Sh3llcod3/HomePage.git
$ cd HomePage/
$ pyenv install 3.8.4
$ pyenv local 3.8.4
$ poetry self:update --preview || poetry self update --preview
$ poetry update
$ poetry install # Add --no-dev if you don't want dev deps
$ poetry shell
$ homepage -ip
$ homepage -df
```

After installing `pyenv`, the lines you add to your `~/.bashrc` may need to be different, please see the [FAQ](#faq--troubleshooting).

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

#### Pyenv fails to install 3.8.4

You may have forgotten to install some crucial `pyenv` dependencies.
If you're using other package managers, check [here](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
for their wiki page. If you're using `apt`, you can simply run:

```bash
$ sudo apt update
$ sudo apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Then retry the `pyenv` installation.

#### Why does HomePage exist?

That is a really good question.
I wanted a simple web app where I could download music from various videos on any
device, without having access to a command line version of `youtube_dl` or resorting
to using questionable sites and apps.

The code is bad at best, but it works and you have the freedom of choice.
Whether you want to use it, is up to you.

#### Why is it not working?

Your version of `youtube_dl` may be out of date. Having a version of `youtube_dl`
that is even one version old can mean your tracks may fail to download. Fortunately,
the library is updated frequently and you can pull in the updates very easily.

If you're using it from PyPi, then:
```shell
$ python3 -m pip install --upgrade youtube_dl gevent Flask --user
$ youtube-dl --rm-cache-dir
```

If you're using it from the `env`, then simply `cd` to the directory you installed it
and run:
```shell
$ poetry update
$ poetry shell
```

> You may want to write some sort of `cron` job to do this every few days or so.

#### Does HomePage scale to multiple users asynchronously?

No. It was never intended to scale in the first place. Neither is it secure in any way.
Therefore, I should stress that you should __NOT__ deploy this to anywhere except your
RFC1918 private/internal network.

#### Does it have Windows support?

Yes. If you can get the latest executables for `lame`, `atomicparsley`, `faac`, `ffmpeg` and
place them inside the project's directory, it should work.

#### Why does it take so long?

This depends on:

- Number of CPU cores
- If the single thread when downloading
- Depends on speed of computer and version of ffmpeg
- Size of download, network speed
- Single track or playlist?

## To-do

- [ ] Add an authentication page.
- [ ] Make site restore state after a download.
- [ ] Save user preferences using cookies.
- [ ] Display past tracks only for that host.
- [ ] Add a separate page for management.
- [ ] Create a system to auto-update `youtube_dl`
- [ ] Make it work on windows and generate executables
