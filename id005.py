import time


def divisible(num, min=1, max=20):
    '''Return whether a number is divisible in the xrange of min to max'''
    for i in xrange(min, max + 1):
        if num % i != 0:
            return False
    return True

if __name__ == '__main__':
    start = time.time()
    current = 2520
    while not divisible(current):
        current += 2520

    elapsed = time.time() - start
    print "%s found in %s seconds" % (current, elapsed)
