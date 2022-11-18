# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def compute():
    n = 2 ** 1000
    ans = 0
    while n > 0:
        curr = n % 10
        n //= 10
        ans += curr
    return ans


if __name__ == "__main__":
	print(compute())