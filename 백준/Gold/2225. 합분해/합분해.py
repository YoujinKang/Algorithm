import sys
input = sys.stdin.readline

MOD = 1000000000

n, k = map(int, input().split())

d = [[0] * 201 for _ in range(201)]
# d[k][n] = 경우의 수
d[0][0] = 1

# d[4][10] 이면, [0, (10을 3개로 쪼갠 것)], [1, (9를 3개로 쪼갠 것)], ..., [10, (0을 3개로 쪼갠 것)]
# d[k][n] = d[k-1][0] + d[k-1][1] + ... + d[k-1][n]
# d[k][n-1] = d[k-1][0] + ... + d[k-1][n-1]
# 따라서 d[k][n] = d[k][n-1] + d[k-1][n]
for i in range(201):
    for j in range(1, 201):
        d[j][i] = (d[j-1][i] + d[j][i-1]) % MOD

print(d[k][n])


