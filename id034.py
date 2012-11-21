from time import clock
from math import factorial


def main():
    start = clock()
    curious = sum([n for n in range(145, 50000) if n == sum([factorial(int(i)) for i in str(n)])])
    print "%s found in %s seconds" % (curious, clock() - start)

if __name__ == '__main__':
    main()
