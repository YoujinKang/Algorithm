import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 0 <= a, b <= n-1
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * n
condition = False

def dfs(v, cnt):
    global condition
    visited[v] = 1
    if cnt == 4:
        condition = True
        return
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0

for i in range(n):
    dfs(i, 0)
    visited[i] = 0
    if condition:
        break

if condition:
    print(1)
else:
    print(0)
