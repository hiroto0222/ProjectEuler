# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

# intuition:
# sum -> n(n + 1) // 2
# brute force

import math
import itertools

def compute():
    for i in itertools.count(1):
        cnt = 0
        curr_sum = i * (i + 1) // 2

        for i in range(1, int(math.sqrt(curr_sum)) + 1):
            if curr_sum % i == 0:
                cnt += 2
        if int(math.sqrt(curr_sum))**2 == curr_sum:
            cnt -= 1
        
        if cnt > 500:
            return curr_sum


if __name__ == "__main__":
	print(compute())