# date: 2020/09/10
# author: psS2mj
# brief: 프로그래머스 월간 코드 챌린지 시즌1 (9월) - 2번

# 풀이과정
from pprint import pprint

n = 4
answer = []
# result = [[0] * n] * n
result = [[0 for x in range(n)] for y in range(n)]

num = 1
x = -1
y = -1

for i in range(n):
    for j in range(i,n):
        if i % 3 == 0:
            x+=1
            y+=1
            # print("대각선으로 가!")
        elif i % 3 == 1:
            y-=1
            # print("y 움직여!")
        else:
            x-=1
            # print("x 움직여!")
        result[x][y] = num
        num+=1

pprint(result, width=5*n)

for i in result:
    for j in i[::-1]:
        if j != 0:
            answer.append(j)

print(answer)

# 제출용 코드
def solution(n):
    answer = []
    result = [[0 for x in range(n)] for y in range(n)]

    num = 1
    x = -1
    y = -1

    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x+=1
                y+=1
            elif i % 3 == 1:
                y-=1
            else:
                x-=1
            result[x][y] = num
            num+=1

    for i in result:
        for j in i[::-1]:
            if j != 0:
                answer.append(j)
                
    return answer