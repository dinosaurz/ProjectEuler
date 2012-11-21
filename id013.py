import time


def parseFile():
    with open("extras/13.txt") as text:
        strings = []
        for line in text.read().split('\n'):
            strings.append(line)

        return strings
    return ''


def main():
    start = time.time()
    numbers = parseFile()

    total = str(sum([int(num) for num in numbers]))
    solution = total[:10]
    elapsed = time.time() - start
    print "%s found in %s seconds" % (solution, elapsed)

if __name__ == '__main__':
    main()
