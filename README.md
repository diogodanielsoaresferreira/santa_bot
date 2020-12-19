![Github repo size](https://img.shields.io/github/repo-size/diogodanielsoaresferreira/santa_bot)
![GitHub license](https://img.shields.io/github/license/diogodanielsoaresferreira/santa_bot)
![GitHub last commit](https://img.shields.io/github/last-commit/diogodanielsoaresferreira/santa_bot)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rasa)

<img src="santa-claus-logo.svg" width=250 height=250 align="right">

# Santa Claus Bot

Talk directly with Santa Claus and tell him what presents you want!


## Usage

Here is an example of a simple conversation flow. The christmas present will be stored in a 
database, along with the person name.

```
Your input -> Hi
Hi, what's your name?
Your input -> My name is Luke
What do you want for Christmas?
Your input -> I want a racing car
Thanks Luke, I will note it down
```


## Instalation

Run the action server in a docker image.

```console
$ docker-compose up
```

In a separate terminal, train and test the santa bot with the following commands.

```console
$ rasa train
$ rasa shell
```


## License
This repo has the Apache 2.0 License.
