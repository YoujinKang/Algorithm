import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    val = int(input())
    if val <= k:
        coins.append(val)

coins = sorted(coins)

# d[k원] = 경우의 수
d = [0] * (k + 1)
d[0] = 1

for coin in coins:
    for i in range(1, k + 1):
        if i >= coin:
            d[i] += d[i-coin]

print(d[k])
