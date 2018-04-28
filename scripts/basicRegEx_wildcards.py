import re

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.') # cat, hat, sat lat mat

nameRegex = re.compile(r'First Name: (.*) Last Name (.*)')
mo = nameRegex.search('First Name: Anthony Last Name: Bendas')
print(mo.group(1)) # Anthony
print(mo.group(2)) # Bendas

nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) # <To serve man>

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) # <To serve man> for dinner.>