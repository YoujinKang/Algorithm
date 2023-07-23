import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())  # 2 <= n, m <= 1000

data = []
q = deque()
for i in range(n):
    line = list(map(int, input().split()))
    data.append(line)
    for j in range(len(line)):
        if line[j] == 1:
            q.append((i, j))

# 동서남북
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    while q:
        vr, vc = q.popleft()
        for i in range(4):
            nr = vr + dr[i]
            nc = vc + dc[i]
            if nr >= 0 and nr < n and nc >= 0 and nc < m:
                if data[nr][nc] == 0:
                    data[nr][nc] = data[vr][vc] + 1
                    q.append((nr, nc))
                    
bfs()
max_val = 0
for ni in range(len(data)):
    if max(data[ni]) > max_val:
        max_val = max(data[ni])
    if 0 in data[ni]:
        max_val = 0
        break

if max_val == 1:
    print(0)
elif max_val == 0:
    print(-1)
else:
    print(max_val - 1)