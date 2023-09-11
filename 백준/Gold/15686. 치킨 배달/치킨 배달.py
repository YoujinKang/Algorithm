from itertools import combinations
import sys
input = sys.stdin.readline
INF = int(1E9)

n, m = map(int, input().split())  # n: 도시 크기, m: 최소 치킨집 수
house = []
chicken = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append((i + 1, j + 1))
        elif row[j] == 2:
            chicken.append((i + 1, j + 1))
        else:
            continue

result = INF  # 도시의 최소 치킨 거리
for comb in combinations(chicken, m):
    tmp = 0  # 도시의 치킨 거리
    for h in house:
        chi_dist_per_house = INF  # 집의 최소 치킨 거리
        for chick in comb:
            dist = abs(h[0] - chick[0]) + abs(h[1] - chick[1])
            chi_dist_per_house = min(chi_dist_per_house, dist)
        tmp += chi_dist_per_house
    result = min(result, tmp)

print(result)

