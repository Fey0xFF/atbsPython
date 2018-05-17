baconFile = open('bacon.txt', 'w') # open file in write mode to write over

baconFile.write('Hello world!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconfile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
print(content)
# prints
# Hello world!
# Bacon is not a vegetable.