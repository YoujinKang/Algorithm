import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())  # n*n크기의 땅, m개의 나무, k년이 지난 후
a = [list(map(int, input().split())) for _ in range(n)]  # 각 칸에 추가되는 양분
b = [tuple(map(int, input().split())) for _ in range(m)]  # (x, y, 나이)

ground = [[5 for _ in range(n)] for _ in range(n)]

# tree[x][y] = [나이1, 나이2, ...]
tree = [[[] for _ in range(n)] for _ in range(n)]
for x, y, z in b:
    tree[x-1][y-1].append(z)

# 동서남북
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

count = len(b)
for _ in range(k):
    for i in range(n):
        for j in range(n):
            dead = 0
            ages = tree[i][j]
            for age in sorted(ages):
                if age <= ground[i][j]:
                    ground[i][j] -= age
                    tree[i][j].pop(0)
                    tree[i][j].append(age + 1)
                else: 
                    dead += (tree[i][j].pop(0)) // 2
                    count -= 1
            ground[i][j] += dead

    for i in range(n):
        for j in range(n):
            ages = tree[i][j]
            for age in ages:
                if age % 5 == 0:
                    for k in range(8):
                        nr, nc = i + dr[k], j + dc[k]
                        if 0 <= nr < n and 0 <= nc < n:
                            tree[nr][nc].insert(0, 1)
                            count += 1
            ground[i][j] += a[i][j]

print(count)
