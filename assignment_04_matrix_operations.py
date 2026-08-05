# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
	matrix = []
	for r in range(1, rows + 1):
		while True:
			raw = input(f"Enter row {r}: ")
			parts = raw.split()
			if len(parts) != cols:
				print(f"Please enter exactly {cols} values.")
				continue
			try:
				row = [int(x) for x in parts]
			except ValueError:
				print("Please enter only integer values.")
				continue
			matrix.append(row)
			break
	return matrix


def print_matrix(matrix):
	if not matrix:
		print("[]")
		return
	# compute column widths
	cols = len(matrix[0])
	widths = [0] * cols
	for row in matrix:
		for j, val in enumerate(row):
			widths[j] = max(widths[j], len(str(val)))

	for row in matrix:
		line = "  ".join(str(val).rjust(widths[j]) for j, val in enumerate(row))
		print(line)


def transpose_matrix(matrix):
	if not matrix:
		return []
	rows = len(matrix)
	cols = len(matrix[0])
	result = [[0 for _ in range(rows)] for _ in range(cols)]
	for i in range(rows):
		for j in range(cols):
			result[j][i] = matrix[i][j]
	return result


def add_matrices(a, b):
	if not a or not b:
		return []
	rows = len(a)
	cols = len(a[0])
	result = [[0 for _ in range(cols)] for _ in range(rows)]
	for i in range(rows):
		for j in range(cols):
			result[i][j] = a[i][j] + b[i][j]
	return result


def multiply_matrices(a, b):
	# a is MxN, b is NxP -> result MxP
	m = len(a)
	n = len(a[0])
	p = len(b[0])
	result = [[0 for _ in range(p)] for _ in range(m)]
	for i in range(m):
		for j in range(p):
			s = 0
			for k in range(n):
				s += a[i][k] * b[k][j]
			result[i][j] = s
	return result


def part_a():
	try:
		rows = int(input("Enter number of rows: "))
		cols = int(input("Enter number of columns: "))
	except ValueError:
		print("Error: please enter integer dimensions.")
		return
	matrix = read_matrix(rows, cols)
	print("\nOriginal Matrix:")
	print_matrix(matrix)
	trans = transpose_matrix(matrix)
	print("\nTransposed Matrix:")
	print_matrix(trans)


def part_b():
	try:
		rows = int(input("Enter number of rows: "))
		cols = int(input("Enter number of columns: "))
	except ValueError:
		print("Error: please enter integer dimensions.")
		return
	print("Enter matrix A:")
	a = read_matrix(rows, cols)
	print("Enter matrix B:")
	b = read_matrix(rows, cols)
	summed = add_matrices(a, b)
	print("\nA + B:")
	print_matrix(summed)


def part_c():
	try:
		m = int(input("Enter number of rows for matrix A: "))
		n = int(input("Enter number of columns for matrix A / rows for matrix B: "))
		p = int(input("Enter number of columns for matrix B: "))
	except ValueError:
		print("Error: please enter integer dimensions.")
		return
	print("Enter matrix A:")
	a = read_matrix(m, n)
	print("Enter matrix B:")
	b = read_matrix(n, p)
	product = multiply_matrices(a, b)
	print("\nA x B:")
	print_matrix(product)


def main():
	print("Matrix Operations — choose part:")
	print("A: Transpose a matrix")
	print("B: Add two matrices")
	print("C: Multiply two matrices")
	choice = input("Choose (A/B/C): ").strip().upper()
	if choice == "A":
		part_a()
	elif choice == "B":
		part_b()
	elif choice == "C":
		part_c()
	else:
		print("Invalid choice.")


if __name__ == "__main__":
	main()


