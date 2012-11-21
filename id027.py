from time import clock
from id003 import isPrime


def eulerTest(a, b, n=2):
    for i in range(1, 41):
        if (n ** 2 + a * n + b) == ((n - i) ** 2 + (n - i) + 41):
            return True
    return False


def primeLength(ab):
    a, b = ab[0], ab[1]
    length = 0
    for i in range(0, 80):
        if not eulerTest(a, b, i):
            break
        length += 1
    return length


def main():
    start = clock()
    bestLen, bestList = 0, []
    for a in range(-1000, 1001):
        if not isPrime(abs(a)):
            continue
        for b in range(-1000, 1001):
            if not isPrime(abs(b)):
                continue
            abLen = primeLength([a, b])
            if abLen > bestLen:
                bestLen, bestList = abLen, [a, b]

    print "%s found in %s seconds" % (bestList[0] * bestList[1], clock() - start)


if __name__ == '__main__':
    main()
