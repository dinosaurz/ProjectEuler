#!/usr/bin/python
'''Project Euler problem 43 Solution'''
from itertools import permutations


def check(pan):
    '''Quick helper'''
    if pan[0] == '0':
        return False

    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        if int(pan[i:i + 3]) % divisors[0] == 0:
            del divisors[0]
    if len(divisors) == 0:
        return True
    return False


def main():
    '''Run the main solution'''
    tests = [''.join(i) for i in permutations('1234567890')]
    print sum([int(pan) for pan in tests if check(pan)])

if __name__ == '__main__':
    main()

