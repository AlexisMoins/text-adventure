# text-adventure

**Disclaimer**: the game and the repo are still in early development phase !

text-adventure is, as its name suggests, a text based adventure on the terminal entirely written in python. The game aims at being modular as almost every aspects of the game can be modified by the users by editing the appropriate configuration files.

## How to play

### Cloning the repository

Start by cloning the repository to get the files on your machine. Alternatively, you can change `~/.text-adventure` to any location you want.

```bash
# Clone and enter the downloaded directory
git clone git@github.com:AlexisMoins/text-adventure.git ~/.text-adventure
```

### Setup the environment

**Note:** This repository relies on multiple python packages. You can find out which ones are used in the `pyprojet.toml` file. To manage my packages, I use [poetry](https://python-poetry.org). If you are not using this tool, you should try to install the packages directly via `pip`.  

As a final note, please notice that the syntax used across the projet is python version **3.10** so you might want to install version 3.10 via python's [official website](https://www.python.org) or via tools like [pyenv](https://github.com/pyenv/pyenv).

```bash
# First, enter the directory
cd ~/.text-adventure

# Using poetry
poetry install && poetry shell
```

### Launching the game

Once the environment is ready, simply launch the main script and you're good to go !

```bash
# Embark on a new adventure !
python main.py
```
