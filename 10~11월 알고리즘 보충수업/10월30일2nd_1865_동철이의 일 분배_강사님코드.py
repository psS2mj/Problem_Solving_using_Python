# idx : 직원 번호
# rate : 누적 성공 확률
def solve(idx,rate):    #선택할 수 있는 모든 경우의 수 고려하기
    global max_rate
    if rate <= max_rate:    #더 곱하더라도 작아짐. 더이상 진행할 필요가 없음
        return
    if idx == N:
        # 모든 직원들이 업무를 선택한 상황
        #각 직원들이 선택한 업무에 대해서, 성공확률 계산하기
        # 직원들이 선택한, 비율을 다 곱해주면 됨
        # 어떤 직원이 어떤 작업을 선택했는지 알아야 함
        # >>작업을 선택을 하면서, 바로 성공확률을 계산하자!
        # print(rate*100)
        if rate > max_rate:
            max_rate = rate
        return
    #가능한 일 중에서 하나를 고른다음, 다음 직원으로 이동
    for i in range(N):
        if check[i] == 0:   # 일이 선택되지 않음
            check[i] = 1
            solve(idx+1,rate * rates[idx][i])
            check[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rates = [list(map(int,input().split())) for _ in range(N)]
    #  0.xxxxx  >>>곱하면 곱할 수록 작아짐. 1을 곱하면 유지,

    for i in range(N):
        for j in range(N):
            rates[i][j] = rates[i][j]/100
    check = [0] * N     #일이 선택되었는지 표시하기 위한 배열
    max_rate = 0
    solve(0,1)
    print("#%d %0.6f" % (tc,round(max_rate*100,6)))