# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

# intuition:
# top down dp


def compute():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [1] + [0] * target
    
    for i in range(len(coins)):
        for j in range(coins[i], target + 1):
            dp[j] += dp[j - coins[i]]
    print(dp)
    return dp[target]


if __name__ == "__main__":
    print(compute())
