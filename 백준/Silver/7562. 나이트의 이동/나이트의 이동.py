import sys
from collections import deque
input = sys.stdin.readline

n_test = int(input())

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

    
def bfs(r, c, kr, kc):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        vr, vc = q.popleft()
        if vr == kr and vc == kc:
            return visited[kr][kc] - 1
        
        for idx in range(len(dr)):
            nr = vr + dr[idx]
            nc = vc + dc[idx]
            if nr >= 0 and nr < l and nc >= 0 and nc < l and visited[nr][nc] == 0:
                visited[nr][nc] = visited[vr][vc] + 1
                q.append((nr, nc))
            

for _ in range(n_test):
    l = int(input())
    r, c = map(int, input().split())
    kr, kc = map(int, input().split())

    visited = [[0] * l for _ in range(l)]
    
    print(bfs(r, c, kr, kc))