import os

os.path.join('usr', 'bin', 'spam') # user/bin/spam

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join('usr/bin/spam', filename))

os.getcwd()
os.chdir('/Users/anthony')
os.getcwd()
os.chdir('/ThisFolderDoesNotExist') # throws an error