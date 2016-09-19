#!/usr/bin/env python2

def trial_division(limit):
    """
    For each number under the limit, try dividing it by every number that it 
    could divide evenly into.  We can tell if one number divides evenly into 
    another by using the modulo (%) operator, which returns the integer 
    remainder after dividing two numbers.
    """
    primes = []

    for candidate in range(2, limit + 1):
        candidate_ok = True

        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                candidate_ok = False
                break

        if candidate_ok:
            primes.append(candidate)

    return primes

def sieve_of_eratosthenes(limit):
    """
    The sieve array contains a boolean value for every number between 2 and 
    the given limit.  The boolean value indicates whether or not that number 
    could be a prime.  At the beginning of the algorithm, every number could 
    be a prime (i.e. the array is True everywhere).  The algorithm works by 
    eliminating more and more numbers until only the primes remain.
    """
    primes = []
    sieve = [True for i in range(limit + 1)]

    for candidate in range(2, limit + 1):
        if sieve[candidate]:
            primes.append(candidate)

            for not_prime in range(2 * candidate, limit + 1, candidate):
                sieve[not_prime] = False

    return primes


def part_1():
    """
    Test the two algorithms above to make sure they actually do return all the 
    prime numbers below a certain limit.  Write your tests using the assert 
    statement, for example:

    >>> assert 1 + 2 == 3

    This will do nothing if the given condition is True and will crash your 
    program if it's False.
    """
    pass

def part_2():
    """
    Plot how long each of the algorithms above takes to finish as the limit 
    increases, say from 1 to 500.
    """
    import time
    start_time = time.time()
    elapsed_time = time.time() - start_time


print "Making sure the prime-finding algorithms work..."
part_1()

print "Plotting how long each algorithm takes..."
part_2()

# Bonus part:
# There are a few ways you could modify the trial division algorithm to make it 
# go faster.  Read the code, think about what it's supposed to do, find places 
# where it's doing more work than it needs to, and see if you can cut out that 
# work to make it go faster.


