# date: 2020/10/23
# author: psS2mj
# brief: BOJ_4344_평균은 넘겠지

C = int(input())
for _ in range(C):
    scores = list(map(int,input().split()))
    N = scores[0] # 학생 수
    sum = 0 # 합계 구하는 용도
    for i in scores[1:]:
        sum += i
    avg = sum / N
    sum = 0 # 평균 넘는 총 학생 수 구하는 용도
    for i in scores[1:]:
        if i > avg:
            sum += 1
    print("{:.3f}%".format(sum/N*100))