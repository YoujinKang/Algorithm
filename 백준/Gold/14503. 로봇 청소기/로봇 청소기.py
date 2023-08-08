import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
# d: [북, 동, 남, 서]
place = []
for _ in range(n):
    place.append(list(map(int, input().split())))
# 0: 청소되지 않은 빈칸, 1: 벽, 2: 청소된 칸

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def rotation(d):
    d -= 1
    if d < 0:
        d = 3
    return d

count = 0
while True:
    rot_count = 0
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if place[r][c] == 0:
        place[r][c] = 2
        count += 1
    # 현재 칸의 주변 4칸 중
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 청소되지 않은 빈 칸이
        if place[nr][nc] != 0:
            rot_count += 1
    # 없는 경우
    if rot_count == 4:
        # 바라보는 방향을 유지한 채로 
        nr = r - dr[d]
        nc = c - dc[d]
        # 한칸 후진할 수 있다면 한칸 후진하고 
        if place[nr][nc] != 1:  # 벽만 아니면 후진할 수 있음
            r, c = nr, nc
            continue
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
    else:  # rot_count < 4
        # 반시계 방향으로 90도 회전한다.
        d = rotation(d)
        # 바라보는 기준으로 앞쪽 칸이 
        nr = r + dr[d]
        nc = c + dc[d]
        # 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        if place[nr][nc] == 0:
            r, c = nr, nc


print(count)