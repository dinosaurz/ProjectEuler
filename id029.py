from time import clock


def main():
    start = clock()
    terms = len(set([a ** b for a in range(2, 101) for b in range(2, 101)]))
    print "%s found in %s seconds" % (terms, clock() - start)

if __name__ == '__main__':
    main()
