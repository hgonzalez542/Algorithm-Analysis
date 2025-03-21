# Authors: Hector Gonzales, Guhan Jeong, Brianna Taylor
# Date: 03/19/2025
# Description: Implementing the binomial coefficient using dynamic programming based on Algorithm 3.2 on page 99.

#--------------------------------------------------------------------------------------
# This program was alot more interesting to create because of the difference in efficiency and thinking
#--------------------------------------------------------------------------------------

# Function to calculate the binomial coefficient using dynamic programming (iterative approach)
def binomial_coefficient_dp(n, k):
    # Create a 2D array to store binomial coefficients
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize the base cases
    for i in range(n + 1):
        dp[i][0] = 1  # Binomial coefficient of (n, 0) is always 1
    for j in range(k + 1):
        dp[j][j] = 1  # Binomial coefficient of (n, n) is always 1
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    return dp[n][k]

# Test the function with n=10 and k=5
n = 10
k = 5
print(f"Binomial Coefficient of ({n}, {k}) is: {binomial_coefficient_dp(n, k)}")
