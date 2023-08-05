import sys
input = sys.stdin.readline

INF = 1E9

n = int(input())
p = [0] + list(map(int, input().split()))

d = [INF] * (1001)
d[0] = 0
# d[구매하고자 하는 카드의 수] = 최소
# d[1] = p[1]
# d[2] = min(d[1] + d[1], p[2])  
#      = min(d[1] + p[1], d[0] + p[2])
# d[3] = min(d[2] + p[1], d[1] + p[2], d[0] + p[3]) 

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = min(d[i], d[i-j] + p[j])

print(d[n])