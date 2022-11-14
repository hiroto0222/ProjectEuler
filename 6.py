# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# intuition:
# brute force
# s1 = (N(N + 1)(2N + 1)) / 6
# s2 = N(N + 1) / 2


def brute_force():
    sum_squares = sum(i**2 for i in range(1, 101))
    square_sum = sum(i for i in range(1, 101))**2
    return square_sum - sum_squares


def compute():
    N = 100
    square_sum = (N * (N + 1) // 2)**2
    sum_squares = (N * (N + 1) * (2 * N + 1)) // 6
    return square_sum - sum_squares


if __name__ == "__main__":
    print(brute_force())
    print(compute())