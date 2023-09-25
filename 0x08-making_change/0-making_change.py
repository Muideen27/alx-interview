#!/usr/bin/python3
""" making change module """


def makeChange(coins, total):
    if total < 1:
        return 0
    if not total or not coins:
        return -1
    coins = sorted(coins)
    count = 0
    change = 0
    for i in range(len(coins) - 1, -1, -1):
        current = coins[i]
        while current + change <= total:
            change += current
            count += 1
    if total != change:
        return -1
    return count
