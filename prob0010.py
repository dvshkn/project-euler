# project euler, problem 10

import math

def is_prime(number):
	ceil = int(math.floor(math.sqrt(number)))

	for i in range(2,ceil+1):
		if number % i == 0:
			return False

	return True


def main():
	sum = 0
	for i in range(2,2000000):
		if is_prime(i) == True:
			sum = sum + i
			print 'new prime %d, sum = %d' % (i, sum)

main()