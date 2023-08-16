import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())  # 1 <= n, m <= 20
board = [list(input().strip()) for _ in range(n)]

coins = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coins.append((i, j))


# board 안에 있는지 확인
def in_board(coin):
    return 0 <= coin[0] < n and 0 <= coin[1] < m


# 벽이면 안가고, 벽 아니면 가고
def is_wall(coin, coin_moved):
    if in_board(coin_moved) and board[coin_moved[0]][coin_moved[1]] == "#":
        return coin
    else:
        return coin_moved


# button
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def get_next(coins):
    coin1, coin2 = coins
    r1, c1 = coin1
    r2, c2 = coin2
    candidates = []
    for i in range(4):
        coin1_moved = (r1 + dr[i], c1 + dc[i])
        coin2_moved = (r2 + dr[i], c2 + dc[i])
        candidates.append((is_wall(coin1, coin1_moved), is_wall(coin2, coin2_moved)))
    return candidates


# 1회 이동
def move(coins, step):
    if step >= 10:
        return 100
    # 갈 수 있는 위치들 찾음
    next_cand = get_next(coins)  # (coin1, coin2)
    vals = []
    for coin1_next, coin2_next in next_cand:
        # 아직 보드에 있다면
        if in_board(coin1_next) and in_board(coin2_next):
            # 이동해서(step+1) 이 이동에 따른 결과값을 vals에 전달
            vals.append(move((coin1_next, coin2_next), step + 1))
        # 둘 다 떨어진다면
        elif not in_board(coin1_next) and not in_board(coin2_next):
            continue  # step 안세고 계속 돌림
        # 하나만 떨어지면
        else:
            vals.append(step + 1)

    return min(vals)


steps = move(coins, 0)
if steps == 100:
    print(-1)
else:
    print(steps)
