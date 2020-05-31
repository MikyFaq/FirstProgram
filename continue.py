
number = 0

while number <= 100:
	number += 1
	if (number % 2) != 0:
		continue;
	print('Чётное число ' +str(number))