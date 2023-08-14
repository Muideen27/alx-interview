#!/usr/bin/python3
''' module for minimum operations '''


def minOperations(n):
    ''' function to get the minimum operations '''
    if n <= 1 or not isinstance(n, int):
        return 0
    x = factorize(n)
    sum = 0
    for i in x:
        sum += i
    return sum


def factorize(n):
    ''' function to factorize a number '''
    temp = n
    x = 2
    li = []
    while x <= temp:
        if temp % x == 0:
            temp = temp / x
            if (is_prime(x)):
                li.append(x)
            else:
                x += 1
        return li


def is_prime(n):
    ''' function to check if a number is prime '''
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
