# project euler, problem 9

# do some maths:
# c^2 = (1000 - a - b)^2
# a^2 + b^2 = (1000 - a - b)^2
# ...
# 2000a + 2000b - 2ab = 1000000
# 1000a + 1000b - ab = 500000

def main():
	a0 = 1
	b0 = 1
	limit = 1000

	for a in range(a0, limit+1):
		for b in range(b0, limit+1):
			if (1000*a + 1000*b - a*b) == 500000:
				print 'candidate pair a=%d, b=%d' % (a, b)

main()