import re


beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!') # match

beginsWithHello.search('Hi my name is') == None # True


endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 7') # match

endsWithNumber.search('Your number is seven') == None # True

beginsEndsWithNumber = re.compile(r'^\d$')
beginsEndsWithNumber.search('7157') # match
beginsEndsWithNumber.search('seven is 7') == None # True