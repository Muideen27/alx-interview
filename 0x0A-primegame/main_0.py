#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))

print("\nWinner: {}\n".format(isWinner(0, [])))

print("Winner: {}".format(isWinner(3, [2, 6, 3])))
print("Winner: {}".format(isWinner(5, [2, 5, 5, 2, 11])))

print("Winner: {}".format(isWinner(7, [2, 0, 0, 0, 0, 0, 0])))
