import time


def parseFile():
    with open("extras/num.txt") as text:
        total = ""
        for line in text.read():
            total += line
    return total


def main():
    start = time.time()
    number = parseFile()
    best_s, curr_s = "", ""
    best_p, curr_p = 0, 0

    for i in xrange(len(number)):
        try:
            curr_p, curr_s = 1, ""
            for j in xrange(5):
                curr_p *= int(number[i + j])
                curr_s += number[i + j]

            if curr_p > best_p:
                best_p = curr_p
                best_s = curr_s
        except:
            break

    elapsed = time.time() - start
    print "str: %s points: %s found in %s seconds" % (best_s, best_p, elapsed)

if __name__ == '__main__':
    main()
