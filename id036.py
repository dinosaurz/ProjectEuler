from time import clock


def is_palindrome(seq, l):
    '''Find whether the sequence is a palindrome'''
    if l < 1:
        return True
    if seq[0] == seq[-1]:
        return is_palindrome(seq[1:l - 1], l - 2)
    return False


def main():
    start = clock()
    total = 0
    for i in xrange(1, 1000000):
        stri = str(i)
        if is_palindrome(stri, len(stri)):
            bini = bin(i)[2:]
            if is_palindrome(bini, len(bini)):
                total += i

    print "%s found in %s seconds" % (total, clock() - start)

if __name__ == '__main__':
    main()
