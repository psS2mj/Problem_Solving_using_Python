# 👨🏻‍🏫 그래프의 dfs와 bfs
# 그래프 => 비선형 구조(❌데이터를 순차적으로 나열하지 않음!!❌)
# 1. 인접행렬: 행과 열의 길이가 각각 정점의 개수와 같은 2차원 배열 (Adjacency Matrix)
# 2. 인접리스트

# 첫 번째 줄에는 정점의 개수 V(Vertex)와 간선의 개수 E(Edge)가 주어진다.
# 5 5
V,E = map(int, input().split())
# 인접행렬을 만들어준다.
adj = [[0]*(V+1) for _ in range(V+1)] # 👨🏻‍🏫정점보다 하나 크게 만들자!
# 1 2
# 1 3
# 1 4
# 2 3
# 2 5
for i in range(E):
    a,b = map(int, input().split())
    # 서로 연결되어 있다.
    adj[a][b] = 1
    adj[b][a] = 1

# for row in adj:
#     print(row)
# [0, 0, 0, 0, 0, 0]
# [0, 0, 1, 1, 1, 0]
# [0, 1, 0, 1, 0, 1]
# [0, 1, 1, 0, 0, 0]
# [0, 1, 0, 0, 0, 0]
# [0, 0, 1, 0, 0, 0]

# dfs를 푸는 방법: 1. 재귀, 2. 스택

# 👨🏻‍🏫먼저 스택으로 풀어봅니다.
def dfs(G,r): # G: Graph
    # stack(LIFO) + 반복문 구조
    stack = list()
    visited = [0]*(V+1)
    stack.append(r)
    visited[r] = 1
    # stack이 비어있지 않는 동안, 갈 수 있는 경로 찾기
    result = list() # 노드 방문 순서를 저장하기 위한 배열
    while stack:
        top = stack.pop()
        result.append(top) # 스택에서 노드를 pop 할 때마다 방문 추가
        # top에 있는 정점에서 갈 수 있는 경로 탐색
        for i in range(V+1):
            # top과 인접해있으면서 방문하지 않은 노드라면, stack에 추가한다.
            if G[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
    return result # 방문 순서가 들어가 있을 것이다.

# result = dfs(adj,1)
# print(result)
# [1, 4, 3, 2, 5]

# 👨🏻‍🏫같은 기능을 하는 함수를 재귀로 만들어봅니다.
def dfs2(visited,G,v): # r 대신 v 사용
    print(v, end=" ")
    visited[v] = 1
    for i in range(V+1):
        if G[v][i] and not visited[i]:
            dfs2(visited,G,i)

# visited = [0]*(V+1)
# result = dfs2(visited,adj,1)
# 1 2 3 5 4
# 👨🏻‍🏫 3이 5보다 숫자가 작아서 3부터 방문

# 👨🏻‍🏫 이제 bfs를 구현해봅니다.
def bfs(G,r):
    queue = list()
    visited = [0]*(V+1)
    queue.append(r)
    visited[r] = 1
    result = list()
    while queue:
        front = queue.pop(0) # 맨 앞에서부터 뺀다.
        result.append(front)
        for i in range(V+1):
            if G[front][i] and not visited[i]: 
                queue.append(i)
                visited[i] = 1
    return result

# result = bfs(adj,1)
# print(result)
# [1, 2, 3, 4, 5]

# 👨🏻‍🏫 이 세 가지를 빠삭하게 익혀야 A형을 취득할 수 있다. 무조건 나온다고 생각하면 된다. 응용할 수 있어야!!!