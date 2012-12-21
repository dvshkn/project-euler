# project euler, problem 12

import math

def get_divisors(number):
	divisors = 1
	ceil = int(math.floor(math.sqrt(number)))
	for i in range(2, ceil):
		if number % i == 0:
			divisors = divisors + 2
	return divisors

def main():
	triangle = 1
	index = 1
	num_divisors = 1
	while num_divisors <= 500:
		index = index + 1
		triangle = triangle + index
		
		num_divisors = get_divisors(triangle)
		#print 'triangle number %d, number of divisors %d' % (triangle, num_divisors)

main()