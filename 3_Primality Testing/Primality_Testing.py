# By Om Nai

import random


# Power function for calculating power that { a ^ (n - 1) % n } -----> { a ^ b % p } in a less time
def power(a, n, p):
    # For fast calculation of power a ^ b
    #         |------------ > a * a ^ (b - 1)       , {if b is odd}
    # a ^ b = |
    #         |------------ > (a ^ 2) ^ (b / 2)     , {if b is even}
    # Now application of modular arithmetic because,
    # {(a + b) % n} = [{(a % n) + (b % n)} % n]
    # {(a * b) % n} = [{(a % n) * (b % n)} % n]
    # And also to save from overflow situation and compress the result (In java, c++, c etc)
    res = 1
    # If a >= p so to make it in range
    a = a % p
    while n > 0:
        # If b is odd then result is updated
        # Doing bitwise end as if it is faster than to test a % 2 == 0 (Does lot computation at processor level)
        if n & 1:
            res = (res * a) % p
        # Just if not odd then general step for odd and even condition both
        n = n >> 1
        a = (a * a) % p
    return res


# Calculating the greatest common divisor
# If a(randomly obtained), n -> a, b As if, for prime numbers gcd is always 1
def gcd(a, b):
    r1 = a
    r2 = b
    while r2 > 0:
        r = r1 % r2
        r1 = r2
        r2 = r
    return r1


# Primality testing function
def isPrime(n):
    # Directly returning for smaller number inputs
    if (n <= 1) or (n == 4):
        return "Composite"
    if n <= 3:
        return "Prime"

    # It is the parameter so that randomly a is selected so that probability of errors are reduced
    k = 500
    while k > 0:
        # This is to be taken (n - 3)
        # This is done because in other languages like C++, java, c etc.
        # random function is not able to generate integers in required range,
        # so it may generate 0 also, and we want a as :
        # 1 < a < (n - 1) so this is done to set the random a in range
        a = 2 + random.randint(0, 922337203685477580) % (n - 3)
        if gcd(n, a) != 1:
            return "Composite"
        if power(a, n - 1, n) != 1:
            return "Composite"
        k -= 1

    return "Prime"
    pass


if __name__ == "__main__":
    print("The passed number is : ", isPrime(246810121))
