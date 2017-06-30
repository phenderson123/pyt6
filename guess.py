import random

num = random.randint(1, 20)
flag = True
guess = 0

print('Take a guess at the number 1-20 :' , end = '')

while flag == True :
	guess = input()
	if not guess.isdigit()
	print('Invalid! Please enter only 1-20')
	break
elif int(guess) < num:
	print('Too low dude:', end ='')
elif int(guess) > num:
	print ('Too darn high:', end = '')
else:
	print('Correct...the number is' + guess)
	flag = False