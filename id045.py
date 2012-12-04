#!/usr/bin/python
from math import sqrt
from id044 import is_penta


def main():
    hex_ = lambda n: n * (2 * n - 1)  # Easy way to calculate hexagonal numbers
    n = 144
    while not(is_penta(hex_(n))):
        n += 1
    print hex_(n)

if __name__ == '__main__':
    main()
