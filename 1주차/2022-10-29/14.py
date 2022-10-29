import math


def solution(n):
    P = 6
    answer = P*n
    gcd = 1
    while 1:
        gcd = n % P
        if gcd == 0:
            break
        n = P
        P = gcd
    gcd = P
    return (answer/gcd)/6

# https://school.programmers.co.kr/learn/courses/30/lessons/120815#
