import sys

input = sys.stdin.readline

n = int(input())
# n x n  체스판에 퀸 n개 경우의 수
# 바로 옆에 없으면 됨

case = 0
row = [0] * n


def is_promissing(x):  # 3
    for i in range(x):  # 0, 1, 2
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            # i = 1 경우 확인
            # row[3] == row[1] 이면 같은 column에 퀸이 놓이게 되므로 false
            # row[3] - row[1] = 3 - 1 이면 대각선상에 퀸이 놓이게 되므로 false
            return False
    return True


def n_queens(r):  # 3
    global case
    # 탈출 조건 설계
    if r == n:
        case += 1
        return
    else:
        for c in range(n):  # 0, 1, 2, 3
            # [r, c] 위치에 퀸 놓음
            row[r] = c  # row[3] = 0, row[3] = 1, row[3] = 2, row[3] = 3 을 각각 하면서 확인
            if is_promissing(r):  # promissing을 만족하는 경우 depth가 증가
                n_queens(r + 1)


n_queens(0)
print(case)
