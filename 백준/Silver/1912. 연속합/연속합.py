import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

d = [0] * (n)
d[0] = data[0]

max_val = d[0]
for i in range(n):
    if i == 0:
        continue
    d[i] = max(d[i-1] + data[i], data[i])
    max_val = max(max_val, d[i])


print(max_val)