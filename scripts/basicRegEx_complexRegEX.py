import re

# hard to read
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')

# easier to read
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            
    (\s|-|\.)?                    
    \d{3}                         
    (\s|-|\.)                     
    \d{4}                         
    (\s*(ext|x|ext.)\s*\d{2,5})?  
    )''', re.VERBOSE)