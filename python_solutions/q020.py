# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def compute():
    val = 1
    for i in range(2, 101):
        val *= i
    
    ans = 0
    while val > 0:
        temp = val % 10
        val //= 10
        ans += temp
    return ans


if __name__ == "__main__":
    print(compute())