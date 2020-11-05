# date: 2020/11/05
# author: psS2mj
# brief: 프로그래머스 월간 코드 챌린지 시즌1 (11월) - 2번

def solution(s):
    answer = [0]*2
    while len(s)>1:
        answer[0] += 1 # 이진 변환 횟수 1 증가
        answer[1] += s.count('0') # 제거할 0의 개수 세기
        s = s.replace("0","") # 모든 0을 제거
        s = bin(len(s))[2:] # 문자열의 길이를 이진법으로 변환     
    return answer