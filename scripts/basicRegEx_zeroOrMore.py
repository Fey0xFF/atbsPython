# RegEX zero or more

 

import re

batRegex = re.compile(r'Bat(wo)*man')

mo1 = batRegex.search('The adventures of Batman')

print(mo1.group())

 

batRegex = re.compile(r'Bat(wo)*man')

mo2 = batRegex.search('The adventures of Batwoman')

print(mo2.group())

 

batRegex = re.compile(r'Bat(wo)*man')

mo3 = batRegex.search('The adventures of Batwowowowoman')

print(mo3.group())

 

# RegEX one or more

catRegex = re.compile(r'Cat(wo)+man')

mo4 = catRegex.search('The adventures of Catman')

print(mo4 == None)

 

mo5 = catRegex.search('The adventures of Catwoman')

print(mo5.group())

 

mo6 = catRegex.search('The adventures of Catwowowowoman')

print(mo6.group())