# Santa Claus Bot

![Github repo size](https://img.shields.io/github/repo-size/diogodanielsoaresferreira/santa_bot)
![GitHub license](https://img.shields.io/github/license/diogodanielsoaresferreira/santa_bot)
![GitHub last commit](https://img.shields.io/github/last-commit/diogodanielsoaresferreira/santa_bot)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rasa)
[![GitHub Super-Linter](https://github.com/diogodanielsoaresferreira/santa_bot/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)


<img src="santa-claus-logo.svg" width=250 height=250 align="right">

Talk directly with Santa Claus and tell him what presents you want!


## Usage

Here is an example of a simple conversation flow. The christmas present will be stored in a
database, along with the person name.

```console
Your input -> Hi
Hi, what's your name?
Your input -> My name is Luke
What do you want for Christmas?
Your input -> I want a racing car
Thanks Luke, I will note it down
```


## Installation

Run the action server in a docker image.

```console
$ docker-compose up
```

In a separate terminal, train and test the santa bot with the following commands.

```console
pip install -r requirements.txt
rasa train
rasa shell
```


## Development

If you wish to install the requirements needed for development, run the following command.

```console
pip install -r requirements-dev.txt
```

## License
This repo has the Apache 2.0 License.
