import sys
input = sys.stdin.readline

MOD = 1000000009

t = int(input())

d = [[0, 0, 0] for _ in range(100001)]
# d[n] = n을 나타낼 때 [1로 끝남, 2로 끝남, 3으로 끝남] 경우의 수 
d[1] = [1, 0, 0] # 1
d[2] = [0, 1, 0] # 2
d[3] = [1, 1, 1] # 2+1, 1+2, 3
# d[4]의 경우는
# 1: d[3]에서 2로 끝나거나 3으로 끝나야 1이 나올 수 있음, 
# 2: d[2]에서 1이나 3으로 끝나야 2가 나올 수 있음, 
# 3: d[1]에서 1이나 2로 끝나야 3이 나올 수 있음
# d[4] = [2, 0, 1] 

for i in range(4, 100001):
    d[i][0] = (d[i-1][1] + d[i-1][2]) % MOD
    d[i][1] = (d[i-2][0] + d[i-2][2]) % MOD
    d[i][2] = (d[i-3][0] + d[i-3][1]) % MOD

for _ in range(t):
    n = int(input())
    print(sum(d[n])  % MOD)