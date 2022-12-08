# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# intuition:
# x x y = z
# as 99 x 99 < 10000 is upperbound,
# hence need product z < 10000, and find all corresponding x, y values

import math


def compute():
    ans = sum(i for i in range(1, 10000) if has_pandigital_prod(i))
    return ans


def has_pandigital_prod(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            temp = str(i) + str(n) + str(n // i)
            if sorted(temp) == "123456789":
                return True
    return False


if __name__ == "__main__":
    print(compute())
