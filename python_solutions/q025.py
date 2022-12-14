# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import itertools


def compute():
    DIGITS = 1000
    f1 = 1
    f2 = 1
    curr = 2
    for i in itertools.count():
        if i > 5000:
            raise RuntimeError("NOT FOUND")

        if len(str(curr)) > DIGITS:
            print("NOT FOUND")
        elif len(str(curr)) == DIGITS:
            return i + 3
        
        f1 = f2
        f2 = curr
        curr = f1 + f2
    

if __name__ == "__main__":
    print(compute())