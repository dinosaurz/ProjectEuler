import time

# Using code from: http://code.jasonbhill.com/python/project-euler-problem-11/


def parseFile():
    with open("extras/11.txt") as text:
        L_org = [line for line in text.read().split('\n')]
        L_sep = [item.split() for item in L_org]
        L_sep = [[int(n) for n in row] for row in L_sep]

        return L_sep
    return []


def main():
    max_prod = 0
    start = time.time()
    A = parseFile()

    # Go through the 20x20 grid
    for i in xrange(20):
        for j in xrange(16):
            # Horizontal products
            prod = A[i][j] * A[i][j + 1] * A[i][j + 2] * A[i][j + 3]
            if prod > max_prod:
                max_prod = prod

            # Vertical products
            prod = A[j][i] * A[j + 1][i] * A[j + 2][i] * A[j + 3][i]
            if prod > max_prod:
                max_prod = prod

    # Diagonal prods... more difficult
    for i in xrange(16):
        for j in xrange(16):
            prod = A[i][j] * A[i + 1][j + 1] * A[i + 2][j +
                                                        2] * A[i + 3][i + 3]
            if prod > max_prod:
                max_prod = prod

    for i in xrange(3, 20):
        for j in xrange(16):
            prod = A[i][j] * A[i - 1][j + 1] * A[i - 2][j +
                                                        2] * A[i - 3][j + 3]
            if prod > max_prod:
                max_prod = prod

    elapsed = time.time() - start
    print "%s found in %s seconds" % (max_prod, elapsed)

if __name__ == '__main__':
    main()
