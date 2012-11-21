import time


def isPrime(num):
    '''
    Return whether a number is prime
    Using Joah Gestenberg's algorithm from www.koding.com

    num: number to be tests
    '''
    if num % 2 == 0:
        return False
    for p in xrange(3, int(num ** 0.5) + 1, 2):
        if num % p == 0:
            return False
    return True


def main():
    """takes numbers and checks for primality."""
    number, primes = 1, 0

    while True:
        if isPrime(number):
            primes += 1
        if primes == 10001:
            break
        number += 2

    print number,

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print "found in %s seconds" % (elapsed)
