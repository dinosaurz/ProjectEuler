import time
start = time.time()

total = 0
for i in xrange(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

elapsed = (time.time() - start)
print "%s found in %s seconds" % (total, elapsed)
