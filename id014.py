import time
counts = {1: 1, 2: 2}


def chainCount(startNum):
    count, num = 0, startNum
    while num != 1:
        count += 1

        if num in counts:
            counts[startNum] = counts.get(startNum, count + counts[num])
            return count + counts[num]

        if num % 2 == 0:
            num /= 2
        else:
            num = (3 * num + 1)


def main():
    start = time.time()

    best, bestCount = 0, 0
    for num in xrange(1, 1000000):
        count = chainCount(num)
        if count > bestCount:
            best, bestCount = num, count

    elapse = time.time() - start
    print "%s found in %s seconds" % (best, elapse)

if __name__ == '__main__':
    main()
