import math


def solution(slice, n):
    if n % slice == 0:
        return n/slice
    else:
        return math.ceil(n/slice)

# https://school.programmers.co.kr/learn/courses/30/lessons/120816
