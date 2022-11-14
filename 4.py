# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# intuition:
# largest possible number -> 999 x 999 = 998001
# smallest possible number -> 100 x 100 = 100000
# largest possible palindromes -> 100001, 


def compute():
    ans = max(i * j
        for i in range(100, 1000)
        for j in range(100, 1000)
        if str(i * j) == str(i * j)[::-1]
    )
    return ans


if __name__ == "__main__":
    print(compute())