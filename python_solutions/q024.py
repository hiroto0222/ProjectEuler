# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools


def compute():
    digits = list(range(10))
    temp = itertools.permutations(digits)
    temp = itertools.islice(temp, 999999, None)
    return int("".join(str(x) for x in next(temp)))

if __name__ == "__main__":
    print(compute())