import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 동서남북
dr = [1, -1, 0, 0]  
dc = [0, 0, 1, -1]

visited = [[0] * m for _ in range(n)]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        vr, vc = q.popleft()
        for i in range(4):
            nr = vr + dr[i]
            nc = vc + dc[i]
            if nr >= 0 and nr < n and nc >= 0 and nc < m:
                if graph[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[vr][vc] + 1
                    q.append((nr, nc))
    return visited[n-1][m-1]

print(bfs(0, 0))