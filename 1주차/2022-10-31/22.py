def solution(num_list):
    even = 0
    odd = 0
    for x in range(len(num_list)):
        if num_list[x] % 2 == 0:
            even += 1
        else:
            odd += 1
    answer = [even, odd]
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/120824
