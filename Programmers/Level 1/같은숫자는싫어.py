# date: 2020/09/16
# author: psS2mj
# brief: 프로그래머스 연습문제_같은 숫자는 싫어

# arr = [1,1,3,3,0,1,1]
arr = [4,4,4,3,3]
answer = []
answer.append(arr[0])

for i in arr:
    if i != answer[-1]:
        answer.append(i)

print(answer)