# date: 2020/11/07
# author: psS2mj
# brief: BOJ_1260_DFS와 BFS

import sys
r = sys.stdin.readline

N, M, V = map(int,r().strip().split()) # N: 정점의 개수(V), M: 간선의 개수(E), V: 시작점
edge = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int,r().strip().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

for i in edge:
    i.sort()

def dfs(G,r,visited):
    stack = [r]
    visited[r] = True
    while stack:
        node = stack.pop()
        for v in G[node]:
            if v not in visited:
                dfs(G,v,visited)
    return visited

from collections import deque
def bfs(G,r,visited):
    que = [r]
    visited[r] = True
    while que:
        node = que.pop(0)
        for v in G[node]:
            if v not in visited:
                que += [v]
                visited[v] = True
    return visited

print(*dfs(edge,V,{}))
print(*bfs(edge,V,{}))