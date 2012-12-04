'''Project Euler problem #67'''
from id018 import findBest


def main():
    '''Find the best path through the triangle'''
    triangle = []
    with open('extras/triangle.txt', 'r') as tFile:
        for line in tFile:
            triangle.append([int(n) for n in line.split()])

    total = findBest(triangle)
    print str(total)

if __name__ == '__main__':
    main()
