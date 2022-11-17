# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

# Intuition:
# recursive brute force using cache


# cache wrapper
def cache(func):
    c = {}
    
    def _wrapper(*args):
        if args not in c:
            c[args] = func(*args)
        return c[args]
    
    return _wrapper


@cache
def count_collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    return 1 + count_collatz(n)


def compute():
    n = 999999
    ans = max(range(1, n + 1), key=count_collatz)
    return ans


if __name__ == "__main__":
    print(compute())