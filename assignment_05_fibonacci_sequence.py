# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_fibonacci(n):
	"""Generate first n Fibonacci numbers as a list using a loop."""
	if n <= 0:
		return []
	seq = [0]
	if n == 1:
		return seq
	seq.append(1)
	for _ in range(2, n):
		seq.append(seq[-1] + seq[-2])
	return seq


def is_fibonacci(number):
	"""Return True if number is a Fibonacci number (non-negative integer)."""
	if number < 0:
		return False
	# generate Fibonacci numbers until >= number
	a, b = 0, 1
	if number == 0:
		return True
	while b < number:
		a, b = b, a + b
	return b == number


def part_a():
	try:
		n = int(input("How many terms? "))
	except ValueError:
		print("Error: please enter a positive integer.")
		return
	if n <= 0:
		print("Error: N must be a positive integer.")
		return
	seq = generate_fibonacci(n)
	print("Fibonacci sequence:", " ".join(str(x) for x in seq))


def part_b():
	try:
		num = int(input("Enter a number to check: "))
	except ValueError:
		print("Error: please enter an integer.")
		return
	if is_fibonacci(num):
		print(f"{num} is a Fibonacci number.")
	else:
		print(f"{num} is NOT a Fibonacci number.")


def main():
	print("Fibonacci — choose part:")
	print("A: Print first N terms")
	print("B: Check membership")
	choice = input("Choose (A/B): ").strip().upper()
	if choice == "A":
		part_a()
	elif choice == "B":
		part_b()
	else:
		print("Invalid choice.")


if __name__ == "__main__":
	main()


