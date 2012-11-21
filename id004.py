import time


def isPalindrome(num):
    num_str = str(num)
    str_beg = num_str[0:3]
    str_end = num_str[3:]
    rev_end = str_end[::-1]

    if str_beg == rev_end:
        return True
    return False


def palindromes(min, max):
    palindromes = []
    for i_one in xrange(min, max):
        for i_two in xrange(min, max):
            product = i_one * i_two
            if isPalindrome(product):
                palindromes.append(product)
    return palindromes

if __name__ == '__main__':
    start = time.time()
    solution = max(palindromes(100, 1000))
    elapsed = time.time() - start
    print "%s found in %s seconds" % (solution, elapsed)
