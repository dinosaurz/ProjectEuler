from time import clock


def main():
    start = clock()
    total = sum([i for i in xrange(3000, 1000000) if sum([int(j) ** 5 for j in str(i)]) == i])
    print "%s found in %s seconds" % (total, clock() - start)

if __name__ == '__main__':
    main()
