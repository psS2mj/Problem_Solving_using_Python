# BFS: DFS와 다른점은?
arr = [
[0,0,0,0,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,0,1,0,0],
[0,0,1,1,2,1,1],
[0,0,1,0,1,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0]
]
N = 7

# 시작점으로부터 목적지까지 최소거리 구하기
# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def bfs(r,c):
    # 먼저 탐색한 경로를 먼저 방문함 (FIFO: First In First Out)
    queue = list() # 👨🏻‍🏫deque(디큐,덱)가 속도 측면에서 좀 더 빠르다. (속도 초과나면 사용해보시길?!)
    visited = [[0]*N for _ in range(N)]
    queue.append((r,c,0)) # 시작점 추가
    visited[r][c] = 1 # 시작점 방문 표시
    while queue: # 큐에 정점 정보가 들어있다면, 계속해서 경로를 탐색!
        hr,hc,dist = queue.pop(0) # h: head

        # 👨🏻‍🏫끝내기 조건
        if arr[hr][hc] == 2:
            return dist

        # 현재 정점으로부터 갈 수 있는 경로를 탐색한다.
        for d in range(4):
            nr = hr + dr[d]
            nc = hc + dc[d]
            # 갈 수 있는 경로일 때
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0 and visited[nr][nc] == 0: # 👨🏻‍🏫arr[nr][nc] == 1이라고 하면 2를 못 찾는다.
                queue.append((nr,nc,dist+1))
                visited[nr][nc] = 1
                # 👨🏻‍🏫break는 하면 안된다. 왜냐? 옆에도 가야하기 때문에! (나머지 경로가 안 들어간다.
                # 모든 경로를 다 갈 수 있다. 그런데 우리가 구할 것은 최소 거리 => 끝내기 조건으로...

    # 👨🏻‍🏫while문을 다 돌 때까지 끝내기 조건(return)에 부합하지 않을 때 여기까지 오게 된다.
    # => 즉, 목적지를 찾지 못했다.
    return -1

print(bfs(1,2)) # 결과: 4