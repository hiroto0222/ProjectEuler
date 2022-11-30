# Euler discovered the remarkable quadratic formula:
# N^2 + N + 41
# Find the product of the coefficients for the quadratic expression that produces the maximum number of primes for consecutive values

import eulerlib, itertools

is_primes = eulerlib.list_primality(1000)

def is_prime(n):
    if n < 0:
        return False
    if n < len(is_primes):
        return is_primes[n]
    else:
        return eulerlib.is_prime(n)


def count_consecutive_primes(ab):
    a, b = ab
    for i in itertools.count():
        n = i * i + i * a + b
        if not is_prime(n):
            return i


def compute():
    ans = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)), key=count_consecutive_primes)
    print(ans)
    return ans[0] * ans[1]
            

if __name__ == "__main__":
    print(compute())
