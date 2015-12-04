# Yu-Gi-Oh Legacy of the Duelist card finder

This will allow you to find out which booster packs contain which cards.
Takes a list of card names, line separated as input.
Thanks to the creators of the Yu-Gi-Oh Legacy of the Duelists Booster Pack Card List from which I built the JSON card list from. You can find the spreadsheet here:
https://docs.google.com/spreadsheets/d/1TazmJLQpekOuWDdxEoun2FPH0Xgh1tiPJdTfioBnj3E/edit?usp=sharing

## Prerequisites

* Git - http://git-scm.com/downloads
* Python 2.7.x - https://www.python.org/download/releases/2.7/

You may already have these installed. You can check by running:

```
python --version
```
```
git --version
```

## How to use

### OS X / Linux

```
git clone git@github.com:marcuspen/ygolotd-card-finder.git
cd ygolotd-card-finder/
python card_finder.py -f my-deck-list.txt
```
The above example works if your card list is named `my-deck-list.txt`.
Ensure that each card on your list is line separated (each card on a different line).

## Updates

If there are any cards missing then please check the spreadsheet where I obtained the data from:
https://docs.google.com/spreadsheets/d/1TazmJLQpekOuWDdxEoun2FPH0Xgh1tiPJdTfioBnj3E/edit?usp=sharing

If you find any errors, feel free to submit an issue via GitHub.
If you want to make changes to the code, then please fork and raise a pull request.

## To-Do

Add instructions for Windows PC's

