from math import factorial
import time


# Using the combination formula the answer is easy to find
# C(n, r) = n! / (r! * (n - r)!)
def main():
    start = time.time()
    n, r = 40, 20
    print (factorial(n) / (factorial(r) * factorial(n - r))),
    print "found in %s seconds" % (time.time() - start)

if __name__ == '__main__':
    main()
