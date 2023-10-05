#!/usr/bin/python3
""" module for prime game task """


def isWinner(x, nums: list):
    """ method to find the winner of x games between maria and ben
    """
    if x < 0 or not nums or x != len(nums):
        return None
    b = 0
    m = 0
    for n in nums:
        if n == 0:
            continue
        arr = [i for i in range(2, n + 1)]
        who = True
        for n in arr:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    who = not who
                    break
            who = not who
        if who:
            b += 1
        else:
            m += 1
    if b > m:
        return 'Ben'
    elif m > b:
        return 'Maria'
    else:
        return None
