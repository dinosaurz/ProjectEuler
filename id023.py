from time import clock


def isAbundant(num):
    def d(a):
        total = 1
        for i in range(2, int(num ** 0.5) + 1):
            if a % i == 0:
                total += i + a / i if (i != (a / i)) else i
        return total

    if num < d(num):
        return True
    return False


def main():
    start = clock()
    total = 0

    abun = set()
    for i in range(1, 20162):  # Based on online findings
        if isAbundant(i):
            abun.add(i)
        if not any((i - a in abun) for a in abun):
            total += i

    print "%s found in %s seconds" % (total, clock() - start)

if __name__ == '__main__':
    main()
