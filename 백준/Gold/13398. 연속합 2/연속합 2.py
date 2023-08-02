import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

d = [[0] * (n) for _ in range(2)]
# d[0][i]: 제거 안한 경우 최대값
# d[1][i]: 제거 한 경우 최대값
d[0][0] = data[0]

max_val = -1E9
for i in range(n):
    if i == 0:
        continue
    # 연속합 + i번째 데이터 or i번째 데이터부터 선택
    d[0][i] = max(d[0][i-1] + data[i], data[i])
    # i번째를 제거 or 이전에 제거된 경우(이미 1번 제거 선택했으므로 다음부터 제거 못함) + i번째 데이터
    d[1][i] = max(d[0][i-1], d[1][i-1] + data[i])
    max_val = max(max_val, d[0][i], d[1][i])

if n > 1:
    print(max_val)
else:
    print(data[0])
                  