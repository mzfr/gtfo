<h1 align="center">GTFObins on terminal</h1>

![gtfo in action](Images/gtfo.jpg)

### Table of content

- [Introduction](#introduction)
- [Installation](#installation)
    + [Without Virtual environment](#without-virtual-environment)
    + [With Virtual environment](#with-virtual-environment)
- [Usage](#usage)
- [Contribution](#contribution)
- [Credit](#credit)

### INTRODUCTION

GTFO is a tool purely written in python to search binaries on [gtfobins](https://gtfobins.github.io/) and [LOLBAS](https://lolbas-project.github.io/)

### Installation

#### Without Virtual environment

You must be using `Python3` to run this project.

To install do the following things:

* `Clone this repository`
    - `git clone https://github.com/mzfr/gtfo`
* `cd gtfo`
* `pip install -r requirements.txt --user`
* `gtfo -h`

#### Without Virtual environment

You must be using `Python3` to run this project.

To install do the following things:

* `Clone this repository`
    - `git clone https://github.com/mzfr/gtfo`
* `cd gtfo`
* `python -m venv name-of-the-venv`
    - Ex: `python -m venv gtfo`
* Activate the virtual environment.
    - `source gtfo/bin/activate`
* `pip install -r requirements.txt`
* `gtfo -h`

### Usage

```
usage: gtfo [-h] (-b BINS | -e EXE | -w LINK | -ls {bins,exe})

optional arguments:
  -h, --help            show this help message and exit
  -b BINS, --bins BINS  Search binaries on GTFOBins
  -e EXE, --exe EXE     Search Windows exe on LOLBAS
  -w LINK, --link LINK  gtfobins link to the page
  -ls {bins,exe}, --list {bins,exe}
                        list all the available binaries
```

To See all the usage option in action checkout the [gallery]

### Gallery

* `gtfo -b ba`
### Contribution

* There are quite a few TODO's in the project. Help me complete those
* Report a bug
* Fix something and open a pull request

In any case feel free to open an issue

## Credits

Thanks to [norbemi](https://twitter.com/norbemi) and [cyrus_and](https://twitter.com/cyrus_and) for creating [GTFOBins](https://gtfobins.github.io/) without that this project won't be in existence.

Also thanks to all the creators of [LOLBAS](https://lolbas-project.github.io/#)

## Say Thanks [![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/mzfr)

If you'd like to :tada: [say thanks](https://saythanks.io/to/mzfr) :smile:
