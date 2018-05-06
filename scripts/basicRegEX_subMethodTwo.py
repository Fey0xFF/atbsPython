import re

agentNameRegex = re.compile(r'Agent (\w)\w*')
agentNameRegex.sub(r'\1****', 'Agent Anthony told Agent Bob that Agent Alice knew Agent Sven was a double agent.')
# A**** told B**** that A**** knew S**** was a double agent.')