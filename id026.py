from time import clock
from id003 import isPrime


def isReptend(p):
    '''Return whether the number is a Full Reptend Prime
       Formula: 10 ** k = 1(mod p) for k = p - 1'''
    if not isPrime(p):
        return False

    k = 1
    while (10 ** k) % p != 1:
        k += 1

    if k == p - 1:
        return True
    return False


def main():
    start, num = clock(), None
    for num in range(999, 1, -2):
        if isReptend(num):
            break
    print "%s found in %s seconds" % (num, clock() - start)

if __name__ == '__main__':
    main()
