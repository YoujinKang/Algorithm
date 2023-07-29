import sys
input = sys.stdin.readline

MOD = 1000000000

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
# dp[자리 수][앞에 오는 숫자] = 경우의 수 저장

# 1 자리 수: 1부터 9까지 모두 1
for i in range(1, 10):
    dp[1][i] = 1

# 2 자리 수: dp[2][0] = 0, dp[2][1~8] = 2, dp[2][9] = 1
# 3 자리 수: dp[3][0]은 2자리에 대하여 1부터 시작하는 수와 같으므로 d[2][1]
# dp[3][1~8]: 1~8 숫자보다 하나 작은 수로 나오거나, 하나 큰 수로 나오거나 -> dp[2][0~7] + dp[2][3~9]
# dp[3][9]: 9다음에 8밖에 못나옴 -> dp[2][8]
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]      
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


print(sum(dp[n]) % MOD)
