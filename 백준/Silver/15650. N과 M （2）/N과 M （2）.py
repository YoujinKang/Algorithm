import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())  # 1 <= m <= n <= 8
# 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열

array = list(range(1, n + 1))
combi = combinations(array, m)
for value in combi:
    for j in range(m):
        print(value[j], end=' ')
    print('')