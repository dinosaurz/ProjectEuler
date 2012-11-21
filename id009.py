import time


def pythagorean():
    triples = []
    for x in xrange(1, 500):
        for y in xrange(1, 500):
            for z in xrange(1, 500):
                if (x * x) == ((y * y) + (z * z)):
                    triples.append([x, y, z])

    return triples


def main():
    product = 0
    start = time.time()
    triples = pythagorean()
    for each in triples:
        a, b, c = each[0], each[1], each[2]
        if (a + b + c) == 1000:
            product = a * b * c
            break

    elapsed = time.time() - start
    print "%s found in %s seconds" % (product, elapsed)

if __name__ == '__main__':
    main()
