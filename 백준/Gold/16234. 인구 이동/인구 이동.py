import sys 
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 동 서 남 북 
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs(i, j):
    q = deque()
    union = [(i, j)]
    q.append((i, j))
    
    while q:
        rr, cc = q.popleft()
        for k in range(4):
            nr = rr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                diff = abs(a[rr][cc] - a[nr][nc])
                if l <= diff <= r:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    union.append((nr, nc))

    return union

date = 0
while True:
    visited = [[0] * n for _ in range(n)]
    move = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                # 주변의 인접한 국가들로 넓게 연합을 확인해야함
                country = bfs(i, j)
                # 국경선이 열려있다면 == union에 저장된 나라가 2개 이상이라면
                if len(country) > 1:
                    # 인구이동이 일어나고
                    move = True
                    # 인구수 계산하고
                    people = sum(a[x][y] for x, y in country) // len(country)
                    # 연합에 인구 분배
                    for x, y in country:
                        a[x][y] = people
    # 국경선이 안열려있으면 끝냄
    if not move:
        break
    # 인구분배가 한차례 끝났다면 date += 1 -> 인구분배 후 다시 국경선을 확인해야함
    else:
        date += 1

print(date)