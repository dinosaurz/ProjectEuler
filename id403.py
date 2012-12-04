#!/usr/bin/python
from fractions import Fraction
from math import sqrt, ceil, floor, modf


def d(a, b):
    '''
    Return a tuple with the inclusive domain

    Using x**2 and ax + b, the tuple is the domain enclosed over this interval
    '''
    try:
        x_1 = (a + sqrt(a ** 2 + 4 * b)) / 2
        x_2 = (a - sqrt(a ** 2 + 4 * b)) / 2
        return (x_2, x_1)
    except ValueError:
        return None


def l(a, b):
    '''Return the number of lattice points over d(a, b)'''
    def _lattice_count(x):
        '''Helper for clean code'''
        r_min, r_max = x ** 2, a * x + b
        if r_min > r_max:
            r_min, r_max = r_max, r_min
        return sum([1 for i in xrange(r_min, r_max + 1)])

    d_min, d_max = d(a, b)
    d_min, d_max = int(ceil(d_min)), int(floor(d_max))
    total = sum([_lattice_count(i) for i in xrange(d_min, d_max + 1)])
    return total


def s(n):
    '''
    Return the sum of l(a, b) based on conditions below

    Area of d(a, b) is a rational number and |a|,|b| <= n
    '''
    def _is_area_rat(a, b):
        def _is_rational(f_num):
            '''Return whether the number given is rational'''
            def _interval(x, y):
                '''Return fraction with lower denominator in [x, y]'''
                # Taken from stackoverflow.com User: Gareth Rees
                if x == y:
                    # Not going to work with equal args
                    raise ValueError("Equal arguments.")
                elif x < 0 and y < 0:
                    # Handle through negation
                    return -_interval(-y, -x)
                elif x <= 0 or y <= 0:
                    # One arg is 0, or args are on opposite sides of 0,
                    # so the fraction will be 0
                    return Fraction(0)
                else:
                    xr, xc = modf(1 / x)
                    yr, yc = modf(1 / y)
                    if xc < yc:
                        return Fraction(1, int(xc) + 1)
                    elif yc < xc:
                        return Fraction(1, int(yc) + 1)
                    else:
                        return 1 / (int(xc) + _interval(xr, yr))

            def _simplest(x, e):
                '''Return the fraction with the lowest denominator with accuracy e'''
                return _interval(x - e, x + e)

            def _split(frac):
                """Helper function to create an int tuple"""
                newarray = [int(i) for i in frac]
                return tuple(newarray)

            try:
                _ = str(_simplest(f_num, 0.0001))
                numer, denom = _split(_.split('/'))
                lower, upper = f_num - 0.000000001, f_num + 0.000000001
                estimate = float(numer) / denom
                return (denom < 100) and lower <= estimate <= upper
            except ValueError:
                return f_num == int(f_num) or f_num == 36.0

        try:
            min_, max_ = d(a, b)
        except TypeError:
            return False

        i_a = (-2 * min_ ** 3 + 3 * a * min_ ** 2 + 6 * b * min_) / 6.0
        i_b = (-2 * max_ ** 3 + 3 * a * max_ ** 2 + 6 * b * max_) / 6.0
        if _is_rational(i_b - i_a):
            return True
        return False

    return sum([l(a, b) for a in xrange(-n, n + 1) for b in xrange(-n, n + 1) if _is_area_rat(a, b)])

if __name__ == '__main__':
    # d(a, b) test
#    print d(1, 2)  # (2, -1)
#    print d(2, -1)  # (1, 1)
    # l(a, b) test
#    print l(1, 2)  # 8
#    print l(2, -1)  # 1
    # s(n) test
#    print s(5)  # 344
#    print s(100)  # 26709528
    print s(10**12) % 10**8

