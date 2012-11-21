from time import clock


def genCorner(n):
    '''Return a list of all corners of a spiral size N'''
    if n == 1:
        return [1]
    prev = genCorner(n - 2)
    curr = []

    for i in range(4):
        if curr:
            curr.append(curr[-1] + (n - 1))
        else:
            curr = [prev[-1] + (n - 1)]

    [prev.append(i) for i in curr]
    return prev


def genSum(n):
    '''Returns the sum of the diagonals of a spiral size N'''
    if n == 1:
        return 1
    return (4 * n ** 2 - 6 * n + 6 + genSum(n - 2))


def main():
    start = clock()
    total = sum(genCorner(1001))
    print "%s found in %s seconds" % (total, clock() - start)
    start = clock()
    total = genSum(1001)  # And order of 10 faster
    print "%s found in %s seconds" % (total, clock() - start)

if __name__ == '__main__':
    main()
