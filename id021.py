from time import clock
from math import sqrt


def divisors(num):
    '''Return the total of proper divisors'''
    rootNum, total = sqrt(num), 1

    for i in range(2, int(rootNum) + 1):
        if num % i == 0:
            total += i + num / i if (i != (num / i)) else i
    return total


def amicables(a):
    '''Return sum of amicable numbers or 0'''
    da = divisors(a)
    if a == divisors(da) and da > a:
        return a + da
    return 0


def main():
    start = clock()
    total = sum([amicables(num) for num in range(2, 10000)])
    print "%s found in %s seconds" % (total, clock() - start)

if __name__ == '__main__':
    main()
