from time import clock


def is_pandigital(seq):
    nums = [str(n) for n in range(1, 10)]
    sseq = sorted([n for n in seq])

    if nums == sseq:
        return True
    return False


def main():
    start = clock()
    products = set()
    for i in range(2, 100):
        start = 1234
        if i > 9:
            start = 123

        for j in range(start, 10000 / i + 1):
            if is_pandigital(str(i) + str(j) + str(i * j)):
                products.add(i * j)

    print "%s found in %s seconds" % (sum(products), clock() - start)

if __name__ == '__main__':
    main()
