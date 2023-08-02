import sys
input = sys.stdin.readline

d = [[0] * (31) for _ in range(31)]
# d[w개수][h개수] = 경우의 수

# h=0개면 w를 선택하는 방법만 존재함
for i in range(1, 31):
    d[i][0] = 1

for i in range(1, 31):
    for j in range(1, i + 1):
        d[i][j] = d[i-1][j] + d[i][j-1]

while True:
    n = int(input())
    if n == 0:
        break
    print(d[n][n])