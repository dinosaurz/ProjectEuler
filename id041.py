#!/usr/bin/python
''' Project Euler problem #41 Solution'''


def is_prime(num):
    '''Test num for a prime trait'''
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_ndigital(num, n):
    '''
    Return whether or not num is an n-digital number

    Arguments:
        num     the number to be tested
        n       the length of number
    '''
    correct = ''.join([str(i) for i in range(1, n + 1)])
    testnum = sorted([i for i in str(num)])

    # Easy hack to get rid of a few values fast...
    if int(testnum[-1]) % 2 == 0:
        return False
    if ''.join(testnum) == correct:
        return True
    return False


def main():
    '''Main function to run the tests'''
    for i in range(7654321, 654321, -2):
        if is_prime(i):
            if is_ndigital(i, len(str(i))):
                print str(i)
                break

if __name__ == '__main__':
    main()

