# A unit fraction contains 1 in the numerator.
# The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# intuition:
# 1 / 7 = 0.142857...
# 10 * 1 / 7 = 1.428571...
# basic algo:
# 1 / 7 -> 10 / 7 -> 1, 3
# 3 / 7 -> 30 / 7 -> 4, 2
# 2 / 7 -> 20 / 7 -> 2, 6
# 6 / 7 -> 60 / 7 -> 8, 4
# 4 / 7 -> 40 / 7 -> 5, 5
# 5 / 7 -> 50 / 7 -> 7, 1
# 1 / 7 -> repeats...
# keep track of seen using hashmap and check for cycle.

import itertools


def compute():
    ans = max(range(1, 10), key=reciprocal_cycle_length)
    return ans


def reciprocal_cycle_length(n):
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = x * 10 % n


if __name__ == "__main__":
    print(compute())