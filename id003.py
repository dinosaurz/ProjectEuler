from math import sqrt
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


def factors(num):
    '''Return array for factors'''
    rootNum = sqrt(num)  # Middle factor
    fact = [1, num]
    curr = 2

    while curr < rootNum:
        if num % curr == 0:
            fact.append(curr)
            fact.append(num / curr)
        curr += 1

    if rootNum == curr:
        fact.append(curr)

    fact.sort()
    return fact

if __name__ == '__main__':
    start = time.time()
    num = 600851475143
    fact = factors(num)

    greatestPrime = 1
    for factor in fact:
        if isPrime(factor) and factor > greatestPrime:
            greatestPrime = factor

    elapsed = time.time() - start
    print "%s found in %s seconds" % (greatestPrime, elapsed)
