#!/usr/bin/python
from math import sqrt


def is_penta(p_num):
    '''Test whether a number is pentagonal'''
    num = (1 + sqrt(1 + 24 * p_num)) / 6.0
    return num == int(num)


def main():
    '''Run the solution'''
    pentas = [(n * (3 * n - 1) / 2) for n in range(2,2400)]
    for i, p_1 in enumerate(pentas):
        for p_2 in pentas[i + 1:]:
            if is_penta(p_1 + p_2) and (p_2 - p_1) in pentas:
                print (p_2 - p_1)
                return

if __name__ == '__main__':
    main()

