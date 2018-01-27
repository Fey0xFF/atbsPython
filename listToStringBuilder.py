# program takes a list and returns a single string concatenation 
# output expected to be 'list[0], list[1], list[2:], and list[-1]
# i.e. spam = ['apples', 'bananas', 'tofu', 'cats']
# returns 'apples, bananas, tofu, and cats'

def stringBuilder(anyList):
  stringOut = '' # define string concatenation variable
  for item in anyList: 
    if item == anyList[-1]: # check for last index 
      stringOut += 'and ' + str(item)
    else: 
      stringOut += str(item) + ', ' # build string one index at a time
  return stringOut  

def main():
  spamString = stringBuilder(spam)
  print(spamString)
  
spam = ['apples', 'bananas', 'tofu', 'cats']
main()