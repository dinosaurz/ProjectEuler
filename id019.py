from time import clock
from math import floor


def weekday(y, m, d):
    """Return day of the week using a Gaussian algorithm"""
    if m == 1 or m == 2:
        y -= 1
    m = ((m + 9) % 12) + 1
    ytwo = y % 100
    yone = (y - ytwo) / 100

    return ((d + floor(2.6 * m - 0.2) + ytwo + floor(ytwo / 4) + floor(yone / 4) - 2 * yone) % 7)


def countSundays(year):
    count = 0
    for mon in range(1, 13):
        if not weekday(year, mon, 1):
            count += 1
    return count


def main():
    start = clock()
    total = sum([countSundays(i) for i in range(1901, 2001)])
    print "%s found in %s seconds" % (total, clock() - start)

if __name__ == '__main__':
    main()
