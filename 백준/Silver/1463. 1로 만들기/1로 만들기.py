n = int(input())
INF = 1e9
d = [INF] * (1000001)
d[0], d[1] = 0, 0

# d[0]은 사용 안함
# d[1] = 0
# d[2] = 1 부터 연산
# d[x] = min(d[x/3], d[x/2], d[x-1]) + 1
for i in range(2, n + 1):
    cand_1 = d[i - 1] + 1
    if i % 2 == 0:
        cand_2 = d[i // 2] + 1
    else:
        cand_2 = INF
    if i % 3 == 0:
        cand_3 = d[i // 3] + 1
    else:
        cand_3 = INF
    d[i] = min([cand_1, cand_2, cand_3])

print(d[n])
