#! python3
# mcb.pyw - saves and loads text to multiple clipboards
# usage: py.exe mcb.pyw save <keyword> - Saves clipboard contents to keyword
# 		 py.exe mcb.pyw <keyword> - loads keyword contents to clipboard
#		 py.exe mcb.pyw list - lists all keywords 

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	# TODO: list keywords and load content

mcbShelf.close()