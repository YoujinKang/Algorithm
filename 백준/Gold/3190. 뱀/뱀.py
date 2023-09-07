import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  # board 크기
k = int(input())  # 사과 개수

board = [[0] * n for _ in range(n)]  # 1이 있는 위치에 사과
board[0][0] = 2   # 2가 있는 위치에 뱀
for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1  # 0, 0 부터이므로

l = int(input())  # 뱀의 방향 변환 횟수
dir_info = {}  # 뱀의 방향 변환 정보 저장
for _ in range(l):
    rot_info = input().rstrip().split()
    dir_info[int(rot_info[0])] = rot_info[1]


def rotate(rot: str) -> int:
    global direction
    if rot == "L":  # dir 값이 1 증가
        direction = (direction + 1) % 4
    else: # dir 값이 1 감소
        direction = (direction - 1) % 4


q = deque()
q.append((0, 0))  # 뱀의 위치 저장

cnt = 0
direction = 3  # 0, 1, 2, 3 = 북, 서, 남, 동
dn = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}
r, c = 0, 0
while True:
    cnt += 1
    dr, dc = dn[direction]
    r += dr
    c += dc
    if r < 0 or r >= n or c < 0 or c >= n:
        break
    if board[r][c] == 1:  # 가려는 위치에 사과가 있으면
        board[r][c] = 2  # 사과 먹음
        q.append((r, c))  # 뱀 위치 추가

    elif board[r][c] == 0:  # 가려는 위치가 비어있으면
        board[r][c] = 2
        q.append((r, c))  # 뱀 위치 추가
        tail_r, tail_c = q.popleft()  # 처음 들어갔던 위치 꺼냄
        board[tail_r][tail_c] = 0  # 꼬리자리가 0이됨

    else:  # 자기 자신인 경우
        break

    if cnt in dir_info.keys():
        rotate(dir_info[cnt])

print(cnt)