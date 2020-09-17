# date: 2020/09/01
# author: psS2mj
# brief: BOJ_2588_곱셈

A = int(input())
B = input()
for i in B[::-1]:
    print(A*int(i))
print(A*int(B))