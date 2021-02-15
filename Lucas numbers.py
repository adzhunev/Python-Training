import functools
import time
import math

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.6f} secs")
        return value
    return wrapper_timer

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
@timer
def lucas_numbers(n):
    # Function to calculate lucas numbers for given number (n)
    if (n == 0):
        return 2
    if (n == 1):
        return 1

    return lucas_numbers(n - 1) + lucas_numbers(n - 2)

# A function to print all prime factors of
# a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i and divide n
        while n % i == 0:
            print(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)

input_number = 60

lucas_number = lucas_numbers(input_number)
print("L(" + str(input_number) + ") = " + str(lucas_number))

print("Prime factors of " + str(lucas_number) + " are: ")
primeFactors(lucas_number)