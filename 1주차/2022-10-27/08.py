import math
def solution(denum1, num1, denum2, num2):
    denum = [(denum1*num2)+(denum2*num1)]
    num =[num1*num2]
    div= math.gcd(denum[0],num[0])
    answer = [denum[0]/div,num[0]/div]
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/120808
