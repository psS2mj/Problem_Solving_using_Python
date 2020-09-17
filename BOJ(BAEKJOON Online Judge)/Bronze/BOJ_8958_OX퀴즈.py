# date: 2020/09/04
# author: psS2mj
# brief: BOJ_8958_OX퀴즈

# 첫 번째 버전
tc = int(input())

for _ in range(tc):
    str = input()
    cnt = 0
    ans = 0
    for i in str:
        if i == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)

# 두 번째 버전
import sys
tc = int(input())
for _ in range(tc):
    str = sys.stdin.readline().rstrip()
    cnt = 0
    ans = 0
    for i in str:
        if i == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)