import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo.group(1))

print(mo.group(2))

print(mo.group(0))

print(mo.group())

# RegEX pipe matching examples

 

import re

heroRegex = re.compile(r'Batman|Tina Fey')

mo1 = heroRegex.search('Batman and Tina Fey')

print(mo1.group())

 

mo2 = heroRegex.search('Tina Fey and Batman.')

mo2.group()

print(mo2.group())

 

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

mo = batRegex.search('Batmobile lost a wheel')

print(mo.group(0))

print(mo.group(1))

print(mo.group())