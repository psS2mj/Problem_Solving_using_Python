# date: 2020/09/11
# author: psS2mj
# brief: BOJ_5543_상근날드

# 첫 번째 풀이방법
burger = []
drink = []

for _ in range(3):
    burger.append(int(input()))
for _ in range(2):
    drink.append(int(input()))

print(min(burger) + min(drink) - 50)

# 두 번째 풀이방법
cost = [int(input()) for x in range(5)]
print(min(cost[:3])+min(cost[3:])-50)