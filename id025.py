from time import clock
fibs = {0: 0, 1: 1, 2: 1}


def fib(num):
    if num in fibs:
        return fibs[num]
    fibs[num] = fib(num - 1) + fib(num - 2)
    return fibs[num]


def main():
    start = clock()
    currnum = 2
    while len(str(fib(currnum))) < 1000:
        currnum += 1

    print "%s found in %s seconds" % (currnum, clock() - start)

if __name__ == '__main__':
    main()
