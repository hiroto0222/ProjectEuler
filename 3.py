# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# intuition:
# every integer n > 1 has a unique factorization as product of primes
# by dividing n repeatedly by its smallest factor (which is prime)
# then the last factor we divide out must be largest prime factor of n
# 71 * 839 * 1471 * 6857 <-

import math

def compute():
    n = 600851475143
    while True:
        p = smallest_prime_factor(n)
        print(p)
        if p < n:
            n //= p
        else:
            return n

def smallest_prime_factor(n):
    assert n >= 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    
    return n


if __name__ == "__main__":
    print(compute())