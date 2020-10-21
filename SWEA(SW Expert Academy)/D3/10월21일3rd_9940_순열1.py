# date: 2020/10/21
# author: psS2mj
# brief: SWEA_9940_순열1 (D3)

T = int(input())
for tc in range(1,T+1):
    answer = "Yes"
    N = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    for i in range(1,N+1):
        if i != nums[i-1]:
            answer = "No"
            break
    print("#{} {}".format(tc,answer))