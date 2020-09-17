# date: 2020/09/11
# author: psS2mj
# brief: 프로그래머스 연습문제_문자열 내 p와 y의 개수

# s = "pPoooyY"
# s = "Pyy"
# s = ""

# 첫 번째 풀이방법
answer = True
Pnum = 0
Ynum = 0

for i in s:
    if i == 'P' or i == 'p':
        Pnum+=1
    elif i == 'Y' or i == 'y':
        Ynum+=1

answer = True if Pnum==Ynum else False

# 두 번째 풀이방법
def solution(s):
    return s.lower().count('p') == s.lower().count('y')