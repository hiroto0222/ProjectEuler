# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Intuition:
# combinatorics problem
# to get to bottom right of N*N grid, it takes exactly N moves right and N moves down in some order.
# hence there are exactly 2N choose N (binomial coefficient) ways of arranging moves
# nCr -> (n!) / (r! * (n - r)!)

def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def compute():
    n, r = 40, 20
    ans = factorial(n) / (factorial(r) * factorial(n - r))
    return int(ans)


if __name__ == "__main__":
	print(compute())