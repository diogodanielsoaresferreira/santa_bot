# Santa Claus Bot
Talk directly with Santa Claus and tell him what presents you want!

<img src="santa-claus-logo.svg" width=125 height=125 align="right">

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

## License
This repo has the Apache 2.0 License.
