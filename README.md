# Santa Claus Bot

![Github repo size](https://img.shields.io/github/repo-size/diogodanielsoaresferreira/santa_bot)
![GitHub license](https://img.shields.io/github/license/diogodanielsoaresferreira/santa_bot)
![GitHub last commit](https://img.shields.io/github/last-commit/diogodanielsoaresferreira/santa_bot)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rasa)
[![GitHub Super-Linter](https://github.com/diogodanielsoaresferreira/santa_bot/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

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
docker-compose up
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
