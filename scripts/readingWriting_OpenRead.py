# opening, reading and reading lines 
helloFile = open('/Users/anthony/hello.txt')
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open('sonnet29.txt')
print(sonnetFile.readlines())