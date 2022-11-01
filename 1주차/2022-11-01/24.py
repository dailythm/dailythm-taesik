def solution(my_string, letter):
    answer = my_string.maketrans({
        letter: '',
    })
    return my_string.translate(answer)

# https://school.programmers.co.kr/learn/courses/30/lessons/120826
