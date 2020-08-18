for number in range(1, 21):
	if number == 4 or number == 13:
		state = 'UNLUCKY'
	elif number % 2 == 0:
		state = 'even'
	else:
		state = 'odd'
	print(f"{number} is {state}!")

for number in range(1, 21):
	state = 'UNLUCKY' if number == 4 or number == 13 else 'even' if (number % 2 == 0) else 'odd'
	print(f"{number} is {state}!")