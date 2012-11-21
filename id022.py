from time import clock


def main():
    start = clock()
    names = None
    with open("extras/names.txt", 'r') as names:
        names = names.read().split(',')
        names = [name.strip('"') for name in names]
        names = sorted(names)

    # Single line solution for the total
    total = sum([sum([(ord(letter) - 64) * (i + 1) for letter in names[i]]) for i in range(len(names))])
    # Multi line solution for total
    # total = 0
    # for i in range(len(names)):
    #     for letter in names:
    #         total += (ord(letter) - 64) * (i + 1)

    print "%s found in %s seconds" % (total, clock() - start)

if __name__ == '__main__':
    main()
