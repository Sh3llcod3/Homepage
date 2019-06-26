# HomePage

HomePage is a trivial flask web app that allows downloading the audio track from almost any internet video.
It is intended to be deployed inside a private network for personal use, so that hosts within the network can access
and download the tracks they want. HomePage is very basic, but it has a Material Design front-end which is
simple and easy to use. HomePage uses `youtube_dl` to download the videos, so quite a few sites are supported.

## Setup & Prerequsites

HomePage should be deployable on almost any Debian-like system that uses the `apt` package manager.
The installation is very simple, assuming `python3.6` or above is present on the system along with `pip`.

```bash
$ git clone https://github.com/Sh3llcod3/HomePage.git
$ cd HomePage/
$ python3 -m pip install -r requirements.txt
$ cd homepage/
$ ./homepage.py -fdip
```

Alternatively, if your system is running an older version of python or you wish to run this project inside
a virtual environment, you can do that too. In fact, this is the __recommended__ method of installing this project.

First, go ahead and install [pyenv](https://github.com/pyenv/pyenv#basic-github-checkout). Then install [poetry](https://github.com/sdispater/poetry).
Once you've installed those, we just to install a few more things.

```bash
$ git clone https://github.com/Sh3llcod3/HomePage.git
$ cd HomePage/
$ poetry self:update --preview || poetry self update --preview
$ pyenv install 3.7.3
$ pyenv local 3.7.3
$ poetry update
$ poetry install
```

After installing `pyenv`, the lines you add to your `~/.bashrc` may need to be different, please see the [FAQ](#faq-&-troubleshooting).

## Usage

Once deployed, the usage is very simple.

## FAQ & Troubleshooting

#### I'm having trouble with the env

You may have inserted the wrong lines in your `~/.bashrc`.
The initialization lines shown on the pyenv repo don't work
well with poetry. Instead, add these lines to the end of the file
and remove any previous line you may have added before
(taking care to ensure you don't remove anything else).

```bash
# Pyenv installation

if [[ -z "$VIRTUAL_ENV" ]]; then
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
fi
```

#### Pyenv fails to install 3.7.3

You may have forgotten to install some crucial `pyenv` dependencies from apt.
Go ahead and install the packages below. If you're using other package managers,
`HomePage` won't work, but [here](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) is their wiki page:

```bash
$ sudo apt update
$ sudo apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

#### Why does Homepage exist in 2019?

That is a really good question. HomePage was originally created for personal use.
I wanted a simple web app where I could download music from various videos on any
device, without having access to a command line version of `youtube_dl` or resorting
to using shady sites and apps.

The code is bad at best, but it is functional and you have the freedom of choice.
Whether you want to use it or not is up to you, but I assumed that people prefer
convenience, so I should probably upload this where more people may be able to take
advantage of this.

## To-do
