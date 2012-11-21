from time import clock


def is_trivial(numer, denom):
    if numer == denom:
        return False

    frac = float(numer) / float(denom)
    numer, denom = str(numer), str(denom)
    if numer[0] == denom[1] and numer[1] != '0' and denom[0] != '0':
        return (float(numer[1]) / float(denom[0]) == frac)
    if numer[1] == denom[0] and numer[0] != '0' and denom[1] != '0':
        return (float(numer[0]) / float(denom[1]) == frac)
    return False


def simplify(numer, denom):
    if denom % numer == 0:
        return 1, denom / numer
    for i in range(2, numer):
        if numer % i == 0 and denom % i == 0:
            numer, denom = simplify(numer / i, denom / i)
    return numer, denom


def main():
    start = clock()
    fractions = []
    for n in range(10, 100):
        for d in range(10, 100):
            if n > d:
                continue
            if is_trivial(n, d):
                fractions.append([n, d])

    numer, denom = 1, 1
    for frac in fractions:
        numer, denom = int(frac[0]) * numer, int(frac[1]) * denom
    number, denom = simplify(numer, denom)

    print fractions
    print '%s found in %s seconds' % (denom, clock() - start)

if __name__ == '__main__':
    main()
