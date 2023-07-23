import sys
import itertools

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 동서남북
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    if graph[r][c] == 1:
        global cnt
        cnt += 1
        graph[r][c] = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                dfs(nr, nc)
        return True
    return False

result = 0
cnt = 0
cnt_list = []
for i, j in list(itertools.product(range(n), range(n))):
    if dfs(i, j) == True:
        result += 1
        cnt_list.append(cnt)
        cnt = 0

print(result)
cnt_list = sorted(cnt_list)
for i in cnt_list:
    print(i)