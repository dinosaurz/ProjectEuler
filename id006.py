import time


def squareSums(max):
    squares = []
    for i in xrange(max + 1):
        squares.append(i * i)
    return sum(squares)


def sumSquares(max):
    sum = 0
    for i in xrange(max + 1):
        sum += i
    return (sum * sum)

if __name__ == '__main__':
    start = time.time()
    max = 100
    diff = (sumSquares(max) - squareSums(max))
    elapsed = time.time() - start
    print "%s found in %s seconds" % (diff, elapsed)
