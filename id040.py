#!/usr/bin/python
'''
Solution to the Project Euler problem #40
'''


def main():
    '''Print the given solution'''
    nums = ''.join([str(num) for num in range(1, 200000)])
    print len(nums)
    total = int(nums[0]) * int(nums[9]) * int(nums[99]) * int(nums[999])
    total *= int(nums[9999]) * int(nums[99999]) * int(nums[999999])
    print str(total)

if __name__ == '__main__':
    main()

