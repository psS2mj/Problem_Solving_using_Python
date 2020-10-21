T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    #1~N 까지의 숫자들이 한 번씩 나왔는지 확인
    #1~N 까지니까 N번 인덱스 까지 사용> N+1 크기 배열 생성
    check = [0]*(N+1)
    for number in numbers:
        check[number] = 1
    # 1~N까지 숫자 N개가 주어진다.
    # 1~N까지 숫자가 하나씩 주어진다 or
    # # 주어지지 않는 숫자가 있던가
    # for i in range(1,len(check)):
    #     if check[i] == 0:
    #         print("#{} No".format(tc))
    #         break
    # # for-else python 문법 :
    # # for 에서 break가 한번도 안걸리면 실행되는 문장
    # else:
    #     print("#{} Yes".format(tc))
    result = True
    for i in range(1,len(check)):
        if check[i] == 0:
            print("#{} No".format(tc))
            result = False
            break
    if result: # 👩🏻 result가 참일 때
        print("#{} Yes".format(tc))

# 👩🏻 공부한 내용
# 한 숫자가 2개 이상 나온다면 반드시 어떤 숫자는 0개 일테니까,
# check 배열에서 하나라도 0이면 순열이 될 수 없지.