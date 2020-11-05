# date: 2020/11/06
# author: psS2mj
# brief: BOJ_1260_DFS와 BFS

N, M, V = map(int,input().split()) # N: 정점의 개수(V), M: 간선의 개수(E), V: 시작점
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int,input().split())
    adj[v1][v2] = 1
    adj[v2][v1] = 1

visited = {}
def dfs(G,r):
    visited[r] = True
    for v in range(1,N+1):
        if G[r][v] == 1 and v not in visited:
            dfs(G,v)
    return visited

def bfs(G,r):
    visited = {}
    queue = [r]
    visited[r] = True
    while queue:
        # front - rear 또는 head - tail
        front = queue.pop(0)
        for v in range(1,N+1):
            if G[front][v] == 1 and v not in visited:
                queue.append(v)
                visited[v] = True
    return visited

print(*dfs(adj,V))
print(*bfs(adj,V))