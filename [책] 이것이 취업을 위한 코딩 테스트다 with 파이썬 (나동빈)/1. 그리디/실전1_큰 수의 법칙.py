# date: 2020/09/25
# author: psS2mj
# brief: 그리디 - 실전 문제 1: 큰 수의 법칙

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
result = 0

# 첫 번째 풀이방법
for _ in range(M):
    for _ in range(K):
        result += nums[0]
        M -= 1
        if M==0:
            break
    result += nums[1]
    M -= 1
    if M==0:
        break

print(result)

# 두 번째 풀이방법
first = nums[0]
second = nums[1]

sum = first*K + second
result += (M//(K+1))*sum + (M%(K+1))*first

print(result)