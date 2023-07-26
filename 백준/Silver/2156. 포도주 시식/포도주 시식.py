import sys 
input = sys.stdin.readline

n = int(input())
q = [0]
for _ in range(n):
    q.append(int(input()))

d = [0] * 10001
# d[1] = q[1]
# d[2] = q[1] + q[2]
# d[3] = max(d[1] + q[3], d[0] + q[2] + q[3], d[2])
# d[4] = max(d[2] + q[4], d[1] + q[3] + q[4], d[3])

for i in range(1, n+1):
    if i == 1:
        d[1] = q[1]
    elif i == 2:
        d[2] = q[1] + q[2]
    else:
        d[i] = max(d[i-2] + q[i], d[i-3] + q[i-1] + q[i], d[i-1])

print(d[n])