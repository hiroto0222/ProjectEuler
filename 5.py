# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# intuition:
# evenly divisible -> x % y == 0
# lowest common multiple of set of all numbers
# LCM(x1, x2, x3, ...) = LCM(... LCM(LCM(x1, x2), x3), ...)


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a / gcd(a, b)) * b


def compute():
    out = 1
    for i in range(2, 21):
        out = lcm(i, out)

    return int(out)


if __name__ == "__main__":
    print(compute())