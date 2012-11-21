import time
memo = {0: 0, 1: 1}


def fib(n):
    if not n in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

if __name__ == '__main__':
    start = time.time()
    for i in xrange(500):
        if fib(i) > 4000000:
            memo[i] = 0
            break

    total = 0
    for i in memo:
        if memo[i] % 2 == 0:
            total += memo[i]
    elapsed = time.time() - start
    print "%s found in %s seconds" % (total, elapsed)
