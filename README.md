# enote2anki
Quick script to convert Evernote cards into Anki flashcard decks

I wanted a way to import a bunch of notes from Evernote (like quotes, notes on books I've read, etc) and the existing tools (https://github.com/brumar/anknotes) seem to have broken with the latest rev of Anki's software. This is a much lamer, simpler hack, but it worked for me.

Usage:
1) select the cards you want to use from Evernote and export them (eg. search, select-all, right-click, Export...) ... choose the Evernote XML format (the 90s is calling, it wants its format back)
2) clone this repo and run `python enote2anki.py [enex file]`
3) import th resulting .txt file into Anki, choose semicolon-delimited (why?), and choose whether you want the card title or note on the front or back, and vice-versa

Notes:
Yes, this is written in Python 2.7 because that's what's on this computer. Feel free to PR updates ;)