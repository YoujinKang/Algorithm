import copy

def rotate_left(matrix):
    r, c = len(matrix), len(matrix[0])
    new_matrix = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new_matrix[j][i] = matrix[i][-j-1]
    return new_matrix


def push_key(key, lock, n):
    for r in range(1, 2 * n):
        for c in range(1, 2 * n):
            temp = copy.deepcopy(lock)
            for i in range(len(key)):
                for j in range(len(key)):
                    temp[r + i][c + j] += key[i][j]
            if check_key(temp):
                return True
    return False


def check_key(matrix):
    idx = len(matrix) // 3
    for r in range(idx, 2 * idx):
        for c in range(idx, 2 * idx):
            if matrix[r][c] != 1:
                return False
    return True

def solution(key, lock):
    n, m = len(lock), len(key)
    ext_lock = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(n, 2 * n):
        ext_lock[i][n:2 * n] = lock[i - n]

    if push_key(key, ext_lock, n):
        return True

    for _ in range(3):
        key = rotate_left(key)
        if push_key(key, ext_lock, n):
            return True

    return False
