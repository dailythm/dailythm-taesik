def solution(array):
    if len(array) == 1:
        return array[0]
    answer = []
    setList = list(set(array))
    for x in setList:
        answer.append(array.count(x))
    if answer.count(max(answer)) > 1:
        return -1
    index = answer.index(max(answer))
    return setList[index]

# https://school.programmers.co.kr/learn/courses/30/lessons/120812
#
