# date: 2020/11/07
# author: psS2mj
# brief: BOJ_1260_DFS와 BFS

from collections import deque

N, M, V = map(int,input().split()) # N: 정점의 개수(V), M: 간선의 개수(E), V: 시작점
adj = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int,input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

def dfs(G,r):
    stack = deque([r])
    visited = {} # dictionary
    while stack:
        node = stack.pop()
        if node not in visited:
            visited[node] = True
            stack.extend(sorted(G[node], reverse=True))
    return visited

def bfs(G,r):
    queue = deque([r])
    visited = {}
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited[node] = True
            queue.extend(sorted(G[node]))
    return visited

print(*dfs(adj,V))
print(*bfs(adj,V))