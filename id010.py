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
    # Start with 1 as 2 is skipped
    start = time.time()
    number, sum = 1, 0

    while number < 2000000:
        if isPrime(number):
            sum += number
        number += 2

    elapsed = time.time() - start
    print "%s found in %s seconds" % (sum + 1, elapsed)

if __name__ == '__main__':
    main()
