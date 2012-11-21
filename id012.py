from math import sqrt
import time


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


def nextTriangle(num):
    return sum([i for i in xrange(num + 1)])


def main():
    start = time.time()
    curr = 10
    triangle = nextTriangle(curr)

    while len(factors(triangle)) < 500:
        curr += 1
        triangle = nextTriangle(curr)

    elapse = time.time() - start
    print "%s found in %s seconds" % (triangle, elapse)

if __name__ == '__main__':
    main()
