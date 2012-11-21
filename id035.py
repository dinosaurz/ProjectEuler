from time import clock
BADDIG = ['0', '2', '4', '5', '6', '8']


def is_circular(num):
    '''Return whether the number is a circular prime'''
    def _rotate(num):
        '''Return a tuple of numbers with rotated digits'''
        numlist = [i for i in str(num)]
        rotate = []

        for i, _ in enumerate(numlist):
            newnum = numlist[i:] + numlist[:i]
            rotate.append(''.join(newnum))

        return rotate

    def _is_prime(num):
        '''Return boolean indicating whether num is prime'''
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    if _is_prime(num):
        for i in BADDIG:
            if i in str(num) and i != str(num):
                return False

        tests = _rotate(num)
        for poss in tests:
            if not _is_prime(int(poss)):
                return False
        return True
    return False


def main():
    start = clock()
    total = sum([1 for i in xrange(2, 1000000) if is_circular(i)])
    print "%s found in %s seconds" % (total, clock() - start)

if __name__ == '__main__':
    main()
