# date: 2020/09/04
# author: psS2mj
# brief: BOJ_3052_나머지

# 첫 번째 버전
from collections import Counter

nums = [0] * 10

for i in range(10):
    nums[i] = int(input()) % 42

print(len(Counter(nums)))

# 두 번째 버전
nums = []

for _ in range(10):
    num = int(input()) % 42
    if num not in nums:
        nums.append(num)

print(len(nums))

# 세 번째 버전
from collections import Counter
nums = [int(input()) % 42 for _ in range(10)]
print(len(Counter(nums)))