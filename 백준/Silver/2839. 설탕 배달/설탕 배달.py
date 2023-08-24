import sys
input = sys.stdin.readline

n = int(input())
d = [float('inf')] * 5001
d[3], d[5] = 1, 1

for i in range(6, 5001):
    d[i] = min(d[i - 3], d[i - 5]) + 1

if d[n] == float('inf'):
    print(-1)
else:
    print(d[n])