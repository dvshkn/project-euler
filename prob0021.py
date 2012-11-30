# project euler, problem 21

import math

def get_divisors(num):
	res = []
	for i in range(int(math.floor(math.sqrt(num))), 0, -1):
		if num % i == 0:
			res.append(i)

			if (num / i) != i and (num / i) != num:
				res.append(num/i)

	return res

def test():
	print get_divisors(20)
	print get_divisors(142)
	print get_divisors(220)
	print get_divisors(284)
	print get_divisors(440)

def main():
	MAX = 10000
	div_sums = []
	amicables = []
	for i in range(1,MAX+1):
		div_sums.append(sum(get_divisors(i)))

	for i in range(1,MAX+1):
		d_i = div_sums[i-1]
		if d_i <= MAX and i != d_i:
			d_j = div_sums[d_i-1]
			if d_j == i:
				print("d(%d) = %d , d(%d) = %d" % (i, d_i, d_i, d_j))
				amicables.append(i)
				amicables.append(d_i)

	print("found amicable pairs: %s" % str(set(amicables)))
	print("sum of amicable pairs: %d" % sum(set(amicables)))

main()
