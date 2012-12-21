# project euler, problem 16

def main():
	big = 2**1000
	big_sum = sum(int(i) for i in str(big))
	print('the big sum = %d' % big_sum)

main()