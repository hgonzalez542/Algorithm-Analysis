# Authors: Hector Gonzalez, Guhan Jeong, Brianna Taylor
# Date: 03/19/2025
# Description: Implementing the binomial coefficient using the divide and conquer method based on Algorithm 3.1 on page 96.

# Function to calculate the binomial coefficient using divide and conquer (recursive approach)
def binomial_coefficient(n, k):
    # Base cases
    if k == 0 or k == n:
        return 1
    # Recursively calculate the binomial coefficient
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

# Test the function with n=10 and k=5
n = 10
k = 5
print(f"Binomial Coefficient of ({n}, {k}) is: {binomial_coefficient(n, k)}")
