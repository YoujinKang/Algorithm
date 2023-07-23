import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())  # 0 <= n, k <= 100000
MAX = 100001

visited = [-1 for _ in range(MAX)]

def bfs():
    q = deque()
    q.append(n)

    while q:
        v = q.popleft()
        if v == k:
            return
        if 2 * v >= 0 and 2 * v < MAX:
            if visited[2 * v] == -1:
                visited[2 * v] = visited[v] 
                q.appendleft(2 * v)
        for i in [v-1, v+1]:
            if i >= 0 and i < MAX:
                if visited[i] == -1:
                    visited[i] = visited[v] + 1
                    q.append(i)

visited[n] = 0
bfs()
print(visited[k])