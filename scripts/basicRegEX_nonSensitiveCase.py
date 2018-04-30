import re

caseSensitiveRegex = re.compile(r'robocop')
mo = caseSensitiveRegex.search('ROBOCOP was here').group() # none

nonCaseSensitiveRegex = re.compile(r'robocop', re.I)
mo = nonCaseSensitiveRegex.search('roBOcop was here').group() #roBOcop