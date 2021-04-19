# date: 2021/04/20
# author: psS2mj
# brief: BOJ_11721_열 개씩 끊어 출력하기

import sys
input = sys.stdin.readline()
len = len(input)
if len < 10:
    print(input)
else:
    len = len//10
    for i in range(len):
        print(input[i*10:i*10+10])
    print(input[len*10:])