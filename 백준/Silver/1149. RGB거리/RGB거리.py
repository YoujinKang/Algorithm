import sys
input = sys.stdin.readline

n = int(input())  # 2 <= n <= 1000
INF = 1000 * 1000

cost = [[0, 0, 0]]
for _ in range(n):
    cost.append(list(map(int, input().split())))

tot_cost = [[0] * 3 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(3):
        tot_cost[i][j] = cost[i][j] + min(tot_cost[i-1][j-1], tot_cost[i-1][j-2])

print(min(tot_cost[n]))
