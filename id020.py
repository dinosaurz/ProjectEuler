from time import clock
from math import factorial


def main():
    start = clock()
    digit = str(factorial(100))
    total = sum([int(i) for i in digit])
    times = clock() - start
    print "%s found in %s seconds" % (total, times)

if __name__ == '__main__':
    main()
