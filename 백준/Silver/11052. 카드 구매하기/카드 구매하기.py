import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))

d = [0] * (1001)
# d[구매하고자 하는 카드의 수] = 최대 금액
# d[1] = p[1]
# d[2] = max(2 * d[1], p[2])  
# d[3] = max(3 * d[1], d[1] + d[2], p[3]) = max(d[1] + d[2], p[3]) 
# d[4] = max(4 * d[1], 2 * d[1] + d[2], d[1] + d[3], 2 * d[2], p[4]) = max(d[1] + d[3], 2 * d[2], p[4])

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i-j] + p[j])

print(d[n])