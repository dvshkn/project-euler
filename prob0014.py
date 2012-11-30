# project euler, problem 14

LOOKUP = {}

def next_number(n):
	if n % 2 == 0:
		return n/2
	else:
		return 3*n+1

def run_sequence(n0):
	n = n0
	seq_len = 1
	while n != 1:
		if LOOKUP.has_key(n):
			seq_len = seq_len + LOOKUP[n] - 1
			break

		n = next_number(n)
		seq_len = seq_len + 1

	LOOKUP[n0] = seq_len

	return seq_len

def main():
	i = 2
	max_len = 0
	while i < 1000000:
		curr_seq_len = run_sequence(i)
		if curr_seq_len > max_len:
			max_len = curr_seq_len
			print('i = %d, length = %d' % (i, curr_seq_len))
		i = i + 1

main()