# Authors: Hector Gonzalez, Guhan Jeong, Brianna Taylor
# Date: 04/30/2025
# Description: This program implements various algorithms for array and matrix operations, including addition, multiplication, and 
# Fibonacci calculation. It also includes functions to create random arrays and matrices, measure execution time, and run tests on the algorithms

import random
import time

# --------------------------
# Basic Algorithm Functions
# --------------------------

# Add all elements of an array
def add_array_elements(array):
    total = 0
    for number in array:
        total += number
    return total

# Multiply every element in a matrix by a scalar value
def multiply_matrix_by_scalar(matrix, scalar):
    size = len(matrix)
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = matrix[i][j] * scalar
    return result

# Multiply two matrices
def multiply_matrices(matrix_a, matrix_b):
    size = len(matrix_a)
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

# Find the nth Fibonacci number using recursion
def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# --------------------------
# Helper Functions
# --------------------------

# Create a random array of a given size
def create_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

# Create a random square matrix of a given size
def create_random_matrix(size):
    return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# Measure how long a function takes to run (in nanoseconds)
def time_function(func, *args):
    start_time = time.perf_counter_ns()
    result = func(*args)
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    return elapsed_time, result

# --------------------------
# Main Testing Function
# --------------------------

def run_tests():
    array_sizes = [10, 50, 100, 200]  # Sizes for arrays and matrices
    fib_numbers = [5, 10, 20, 25]     # Values for Fibonacci tests

    print("\n--- Testing Array and Matrix Algorithms ---")
    for size in array_sizes:
        array = create_random_array(size)
        matrix_a = create_random_matrix(size)
        matrix_b = create_random_matrix(size)
        random_scalar = random.randint(1, 10)

        add_time, _ = time_function(add_array_elements, array)
        scalar_mult_time, _ = time_function(multiply_matrix_by_scalar, matrix_a, random_scalar)
        matrix_mult_time, _ = time_function(multiply_matrices, matrix_a, matrix_b)

        print(f"\nInput Size: {size}")
        print(f"  ➔ Add Array Elements Time: {add_time} ns")
        print(f"  ➔ Scalar-Matrix Multiplication Time: {scalar_mult_time} ns")
        print(f"  ➔ Matrix-Matrix Multiplication Time: {matrix_mult_time} ns")

    print("\n--- Testing Recursive Fibonacci Algorithm ---")
    for n in fib_numbers:
        fib_time, _ = time_function(recursive_fibonacci, n)
        print(f"  ➔ Fibonacci({n}) Time: {fib_time} ns")

# --------------------------
# Run the Program
# --------------------------

if __name__ == "__main__":
    run_tests()
