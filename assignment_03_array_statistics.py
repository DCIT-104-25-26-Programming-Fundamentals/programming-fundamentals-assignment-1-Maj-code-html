# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
	total = 0
	for n in numbers:
		total += n
	return total


def calculate_average(numbers):
	if len(numbers) == 0:
		return 0
	return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
	if len(numbers) == 0:
		return None
	max_val = numbers[0]
	for n in numbers[1:]:
		if n > max_val:
			max_val = n
	return max_val


def find_minimum(numbers):
	if len(numbers) == 0:
		return None
	min_val = numbers[0]
	for n in numbers[1:]:
		if n < min_val:
			min_val = n
	return min_val


def main():
	try:
		n = int(input("How many numbers? "))
	except ValueError:
		print("Error: Please enter a positive integer for the count.")
		return

	if n <= 0:
		print("Error: Number of elements must be a positive integer.")
		return

	numbers = []
	for i in range(1, n + 1):
		while True:
			try:
				val = float(input(f"Enter number {i}: "))
				break
			except ValueError:
				print("Please enter a valid number.")
		# store as int when it's integral
		if val.is_integer():
			val = int(val)
		numbers.append(val)

	print("\nResults:")
	print(f"Sum:     {calculate_sum(numbers)}")
	avg = calculate_average(numbers)
	# show integer-like averages as int when appropriate
	if avg.is_integer():
		avg = int(avg)
	print(f"Average: {avg}")
	print(f"Maximum: {find_maximum(numbers)}")
	print(f"Minimum: {find_minimum(numbers)}")


if __name__ == "__main__":
	main()


