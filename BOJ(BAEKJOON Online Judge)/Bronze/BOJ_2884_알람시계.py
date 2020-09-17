# date: 2020/09/03
# author: psS2mj
# brief: BOJ_2884_알람 시계

h, m = map(int, input().split())

if m < 45:
    if h == 0:
        h = 23
    else:
        h -= 1
    m += 15
else:
    m -= 45
    
print(h, m)