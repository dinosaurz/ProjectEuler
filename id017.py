import time

numbers = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
           7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
           12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
           16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
           20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
           70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand"}


def singleDigit(num):
    return numbers[num]


def doubleDigit(num):
    if num in numbers:
        return numbers[num]
    num1, num2 = str(num)[0], str(num)[1]
    return doubleDigit(int(str(num)[0] + '0')) + singleDigit(int(str(num)[1]))


def tripleDigit(num):
    if num % 100 == 0:
        return singleDigit(int(str(num)[0])) + numbers[100]
    return (tripleDigit(int(str(num)[0] + '00')) + "and" + doubleDigit(int(str(num)[1] + str(num)[2])))


def count(num):
    if len(str(num)) == 1:
        return sum([1 for n in singleDigit(num)])
    if len(str(num)) == 2:
        return sum([1 for n in doubleDigit(num)])
    if len(str(num)) == 3:
        return sum([1 for n in tripleDigit(num)])
    if len(str(num)) == 4:
        return len("onethousand")  # Account for the 1000 that isn't added
    return 0


def main():
    start = time.time()
    total = sum([count(num) for num in xrange(1, 1001)])
    print "%s found in %s seconds" % (total, time.time() - start)

if __name__ == '__main__':
    main()
