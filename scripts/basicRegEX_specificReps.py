# RegEX specific repetitions

 

import re

haRegex = re.compile(r'(Ha){3}')

mo1 = haRegex.search('HaHaHa')

print(mo1.group())

 

mo2 = haRegex.search('Ha')

print(mo2 == None)

 

 

# difference with '?' flag

greedyHaRegex = re.compile(r'(Ha){3,5}')

mo1 = greedyHaRegex.search('HaHaHaHaHa')

print(mo1.group())

 

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')

 

mo2 = nongreedyHaRegex.search('HaHaHaHaHa')

print(mo2.group())