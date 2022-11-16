# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# intuition:
# sieve of Eratosthenes is the most efficient way to get primes numbers for limit n
# 1. mark all the numbers which are divisible by 2 and are greater than or equal to the square of it. 
# 2. mark all the numbers which are divisible by 3 and are greater than or equal to the square of it. 

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    
    ans = 0
    for p in range(2, num+1):
        if prime[p]:
            ans += p
    return ans


def compute():
    return SieveOfEratosthenes(1999999)


if __name__ == "__main__":
    print(compute())