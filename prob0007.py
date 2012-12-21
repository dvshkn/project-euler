# project euler, problem 7

import math

def is_prime(number):
	ceil = int(math.floor(math.sqrt(number)))

	for i in range(2,ceil+1):
		if number % i == 0:
			return False

	return True


def main():
	x = 2
	count = 1

	while count < 10001:
		x = x + 1
		if is_prime(x) == True:
			count = count + 1
			print 'prime #%d is %d' % (count, x)


main()