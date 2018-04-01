#define the collatz sequence
def collatz(number):
	if number % 2 == 0:
		number = round(number / 2)
		print(number)
		return number
	elif number % 2 > 0:
		number = round(number*3 + 1)
		print(number)
		return number 

while True:
  print('Please enter an integer to perform a collatz sequence on it:')
  try: # test for int
    num = int(input())
    break
  except ValueError: # accept incorrect input and run through input again
    print('You must enter an integer, try again.')
    continue

print('\nThe collatz sequence to your answer is as follows:')
while num != 1:
  num = collatz(num)