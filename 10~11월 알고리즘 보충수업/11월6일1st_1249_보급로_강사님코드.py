import heapq
def dijkstra():
    #인접 방향, 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    #다익스트라 : 시작지점으로 부터 각 정점까지 최소 비용을 저장하는 배열 만들기
    #각 정점이 이차원 배열의 모든 요소가 되므로, 비용저장 배열도 이차원 배열로 만든다.
    #최소비용 저장 배열
    INF = float('inf')
    weight = [[INF] * N for _ in range(N)]
    weight[0][0] = 0    #시작정점에서 비용은 0
    #다익스트라 알고리즘 : 각 정점까지 갈 수 있는 비용중 최소 비용으로 갈 수있는 정점의 비용을 확정
    #                 최소 비용을 쉽게 얻기 위해서 heapq를 사용
    queue = list()
    #(정점까지 비용,row,column),
    # heapq는 요소중 첫번째 요소의 값을 이용해서 최소값을 찾는다.
    heapq.heappush(queue,(weight[0][0],0,0))
    while queue:
        #queue에 있는 좌표중, 최소비용 좌표를 가져옴
        cw,cr,cc = heapq.heappop(queue)

        #해당 정점으로 가는 비용은 확정된다.
        # 해당 정점으로 인해 영향을 받는 정점으로 가는 비용 재계산
        for i in range(4):
            nr,nc = cr+dr[i],cc+dc[i]
            if 0<= nr<N and 0<=nc < N:
                # (cr,cc)에서 (nr,nc)으로 가는 비용 계산
                tmp_cost = cw + arr[nr][nc]
                #만약 계산한 비용이, 기존 경로의 비용보다 더 싸다면,
                if tmp_cost < weight[nr][nc]:
                    #비용 업데이트 및 새롭게 비용 계산 되었으니 queue에 추가
                    weight[nr][nc] = tmp_cost
                    heapq.heappush(queue,(weight[nr][nc],nr,nc))

    #모든 정점에 대해서 비용이 계산되었다면, 목적지의 비용을 반환
    return weight[N-1][N-1]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    result = dijkstra()
    print("#{} {}".format(tc,result))