from time import clock


def get_nine(num):
    '''Returns the pandigital product'''
    def _is_pandigital(num_str):
        '''For readability'''
        if len(num_str) > 9:
            return False
        if ''.join(sorted(num_str)) == '123456789':
            return True
        return False

    products = []
    while len(''.join(products)) < 9:
        products.append(str(num * (len(products) + 1)))

    if _is_pandigital(''.join(products)):
        return int(''.join(products))
    return 0


def main():
    start = clock()
    best = max([get_nine(i) for i in range(9000, 100000)])
    print "%s found in %s seconds" % (best, clock() - start)

if __name__ == '__main__':
    main()
