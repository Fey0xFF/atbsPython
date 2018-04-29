import re


noNewLineRegex = re.compile('.*')
noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law').group()
# Serve the public trust.

newLineRegex = re.compile('.*', re.DOTALL)
newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law').group()
# Serve the public trust.\nProtect the innocent.\nUphold the law