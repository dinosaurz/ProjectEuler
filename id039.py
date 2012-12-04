'''Project Euler Problem # 039'''


def solutions(perim):
    '''Return number of solutions for the perimeter'''
    def _is_right(sides):
        '''Use tuple of sides to determine legality'''
        aside, bside, cside = sides
        if aside ** 2 + bside ** 2 == cside ** 2:
            return True
        return False

    count = 0
    for bside in range(1, perim / 2):
        aside = (perim * (perim - 2 * bside)) / (2 * (perim - bside))
        if _is_right((aside, bside, perim - aside - bside)):
            count += 1
    return count


def main():
    '''Run the solutions to find the best'''
    best_perim, best_side = 0, 0
    for perim in range(1, 1001):
        side = solutions(perim)
        if best_side < side:
            best_perim, best_side = perim, side

    print "%s" % (best_perim)

if __name__ == '__main__':
    main()

