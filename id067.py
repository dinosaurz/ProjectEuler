from id018 import findBest
from time import clock


def main():
    triangle = []
    with open('extras/triangle.txt', 'r') as tFile:
        for line in tFile:
            triangle.append([int(n) for n in line.split()])

    start = clock()
    total = findBest(triangle)
    times = clock() - start
    print "%s found in %s seconds" % (total, times)

if __name__ == '__main__':
    main()
