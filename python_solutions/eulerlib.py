from math import sqrt

# checks whether given input n is prime
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


# returns list of true or false indicating whether each number is prime.
# for 0 <= i <= n, result[i] is True if i is prime, else False
def list_primality(n: int) -> list[bool]:
    res = [True] * (n + 1)
    res[0] = res[1] = False
    for i in range(int(sqrt(n)) + 1):
        if res[i]:
            for j in range(i * i, len(res), i):
                res[j] = False
    return res


# returns all prime numbers <= n
def list_primes(n: int) -> list[int]:
    return [i for (i, isPrime) in enumerate(list_primality(n)) if isPrime]