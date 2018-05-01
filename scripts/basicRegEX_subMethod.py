import re

namesRegex = re.compile(r'Agent \w+')
namesRegex.search('CENSORED', 'Agent Anthony gave the secret documents to Agent Bob')
# 'CENSORED gave the secret documents to CENSORED'