import sys
input = sys.stdin.readline

n = int(input())
data = [[0]]
for _ in range(n):
    data.append(list(map(int, input().split())))

d = [[] for _ in range(n + 1)]
d[0] = [0]
# d[1] = data[1]
# d[2] = [d[1][0] + data[2][0], d[1][0] + data[2][1]]
# d[3] = [d[2][0] + data[3][0], d[2][0] + data[3][1], d[2][1] + data[3][1], d[2][1] + data[3][2]]

for i in range(1, n + 1):
    d[i] = data[i]
    for j in range(i): 
        if j == 0:
            d[i][j] += d[i-1][j]
        elif j == i-1:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j-1], d[i-1][j])


print(max(d[n]))
