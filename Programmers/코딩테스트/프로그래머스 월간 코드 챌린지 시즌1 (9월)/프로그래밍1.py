# date: 2020/09/10
# author: psS2mj
# brief: 프로그래머스 월간 코드 챌린지 시즌1 (9월) - 1번

# 풀이과정
from itertools import combinations

numbers = [2,1,3,4,1]
answer = []

temp = list(combinations(numbers, 2))

for i, j in temp:
    num = i + j
    if num not in answer:
        answer.append(num)

answer.sort()
print(answer)

# 제출용 코드
from itertools import combinations
def solution(numbers):
    answer = []
    temp = list(combinations(numbers, 2))

    for i, j in temp:
        num = i + j
        if num not in answer:
            answer.append(num)

    answer.sort()
    return answer