# 완전탐색 -> 멱집합(부분집합)
# 특정한 조건을 만족하는 부분집합

# 100만이기 때문에 시간이 오래 걸리지 않는다?!
T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    heights = list(map(int,input().split()))
    INF = float('inf')
    min_v = INF
    # 전체 직원의 모든 부분집합 구하기
    def solve(idx,tmp_sum):
        global min_v
        if tmp_sum >= min_v:
            return

        if idx == N:
            if tmp_sum >= B and min_v > tmp_sum: #선반보다 키가 큼
                min_v = tmp_sum
            return
        #직원이 부분집합에 포함 O
        solve(idx+1,tmp_sum + heights[idx])
        # 직원이 부분집합에 포함 X
        solve(idx + 1, tmp_sum)

    solve(0,0)
    print("#{} {}".format(tc,min_v - B))