from time import clock


def main():
    start = clock()
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    diffs = [1] + [0] * 200
    for coin in coins:
        for i in range(coin, 201):  # All coins fit evenly into 200
            diffs[i] += diffs[i - coin]  # Use memorization
    print "%s found in %s seconds" % (diffs[200], clock() - start)

if __name__ == '__main__':
    main()
