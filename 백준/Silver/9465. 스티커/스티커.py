import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    data = []
    for j in range(2):
        data.append([0])
        data[j].extend(list(map(int, input().split())))

    d = [[0] * (n + 1) for _ in range(2)]
    # d[row][column] = 이 스티커를 사용할 때 점수의 최대값

    d[0][1] = data[0][1]
    d[1][1] = data[1][1]

    if n >= 2:
        for i in range(2, n + 1):
            d[0][i] = max(d[0][i-1], d[1][i-1] + data[0][i], d[1][i-2] + data[0][i])
            d[1][i] = max(d[1][i-1], d[0][i-1] + data[1][i], d[0][i-2] + data[1][i])
        
    print(max(d[0][n], d[1][n]))