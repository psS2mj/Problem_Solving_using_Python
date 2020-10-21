# date: 2020/10/21
# author: psS2mj
# brief: SWEA_1204_[S/W 문제해결 기본] 1일차 - 최빈수 구하기 (D2)

T = int(input())
for _ in range(T):
    tc = int(input())
    scores = list(map(int,input().split()))
    cnt = [0]*101
    for i in scores:
        cnt[i] += 1

    m = max(cnt)
    print("#{} {}".format(tc,max([i for i,v in enumerate(cnt) if v == m])))