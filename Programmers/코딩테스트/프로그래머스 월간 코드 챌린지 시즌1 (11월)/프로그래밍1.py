# date: 2020/11/05
# author: psS2mj
# brief: 프로그래머스 월간 코드 챌린지 시즌1 (11월) - 1번

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += (a[i])*(b[i])
    return answer