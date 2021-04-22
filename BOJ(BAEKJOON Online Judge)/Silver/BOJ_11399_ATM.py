# date: 2021/04/23
# author: psS2mj
# brief: BOJ_11399_ATM

N = int(input())
waiting_times = list(map(int,input().split()))
waiting_times.sort() # 인출하는 데 걸리는 시간을 오름차순으로 정렬

time = 0
for i in range(N):
    time += waiting_times[i] * (N-i)
print(time)