# date: 2021/04/22
# author: psS2mj
# brief: BOJ_11047_동전 0

N, K = map(int, input().split())
cnt = 0 # 필요한 동전의 최소 개수

# 동전의 가치를 배열 뒤에서부터 차례대로 저장
coins = [0]*N
for i in range(N):
    coins[N-1-i] = int(input())

idx = 0
while K > 0:
    cost = coins[idx]
    if K >= cost:
        div = K//cost
        cnt += div
        K -= cost*div
    idx += 1

print(cnt)