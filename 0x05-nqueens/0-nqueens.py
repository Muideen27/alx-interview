#!/usr/bin/python3
'''N Queens Challenge'''
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)

    all_qs = []
    queens = []
    stop = False
    r = 0
    c = 0
    while r < n:
        goback = False
        while c < n:
            safe = True
            for qn in queens:
                col = qn[1]
                if(col == c or col + (r - qn[0]) == c or
                        col - (r - qn[0]) == c):
                    safe = False
                    break
            if not safe:
                if c == n - 1:
                    goback = True
                    break
                c += 1
                continue
            qns = [r, c]
            queens.append(qns)
            if r == n - 1:
                all_qs.append(queens[:])
                for qn in queens:
                    if qn[1] < n - 1:
                        r = qn[0]
                        c = qn[1]
                for i in range(n - r):
                    queens.pop()
                if r == n - 1 and c == n - 1:
                    queens = []
                    stop = True
                r -= 1
                c += 1
            else:
                c = 0
            break
        if stop:
            break
        if goback:
            r -= 1
            while r >= 0:
                c = queens[r][1] + 1
                del queens[r]
                if c < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    for idx, val in enumerate(all_qs):
        if idx == len(all_qs) - 1:
            print(val, end='')
        else:
            print(val)
    print()
