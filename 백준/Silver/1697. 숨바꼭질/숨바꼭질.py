import sys
from collections import deque

MIN = 0
MAX = 100000

n, k = map(int, sys.stdin.readline().split())
visited = [0 for i in range(MAX+1)]

def bfs(now):
    q = deque([now])
    while q:
        now = q.popleft()
        if now == k:
            return visited[now]
        # possible position x-1, x+1, 2x 
        for next_x in (now-1, now+1, 2*now):
            if MIN <= next_x <= MAX and not visited[next_x]:
                visited[next_x] = visited[now] + 1
                q.append(next_x)

print(bfs(n))