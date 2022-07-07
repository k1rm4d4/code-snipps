# Prints Fibonacci sequence, upto the given input number:
# Fibonacci sequence:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34......

def print_sequence(max_limit):
	"""Prints the Fibonacci sequence when given a maximum limit.
		- max_limit: Upper limit to the sequence. Only terms less than or equal to will be printed."""
	n = 0
	term = 0
	while term <= max_limit:
		# print with term number
		# print(n, " ", term)
		# print only terms
		print(term)
		n +=1
		term = get_term(n)


def get_term(n):
	"""Calculates the term in the sequence from given position n
		- n:  non-negative integer"""
	if n == 0:
		return 0
	elif n == 1:
		return	1
	else:
		return get_term(n - 2) + get_term(n - 1)


# Get User Input:
user_input = int(input("Please Enter upper limit number for the Fibonacci Sequence:"))		

# print("Entered upper limit: ", user_input)

print_sequence(user_input)

# for i in range(user_input):
# 	print(i, " ", get_term(i))

