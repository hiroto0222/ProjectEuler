# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from math import sqrt


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True


def compute():
    cnt = 10001
    x = 2
    while cnt > 0:
        if isPrime(x):
            cnt -= 1
        if cnt == 0:
            return x 
        x += 1


if __name__ == "__main__":
    print(compute())