import sys
input = sys.stdin.readline

n = int(input())
d = [-1] * 5001
d[3], d[5] = 1, 1

for i in range(6, 5001):
    if d[i - 3] > 0:
        d[i] = d[i - 3] + 1
    if d[i - 5] > 0:
        if d[i] == -1:
            d[i] = d[i - 5] + 1
        else:  # d[i-3] 이 먼저 돌아간 경우
            d[i] = min(d[i], d[i-5] + 1)

print(d[n])