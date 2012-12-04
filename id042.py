#!/usr/bin/python
'''Solution to Project Euler problem #42'''
from string import ascii_uppercase as alpha


def main():
    triangles = [(n * (n + 1) // 2) for n in range(19)]
    letterval = dict(zip(alpha, range(1, 27)))
    commonwords = []

    with open("./extras/words42.txt", "r") as words:
        wordlist = words.read().split(',')
        commonwords = [word.strip('"') for word in wordlist]

    print sum([1 for word in commonwords if sum([letterval[x] for x in word]) in triangles])

if __name__ == '__main__':
    main()

