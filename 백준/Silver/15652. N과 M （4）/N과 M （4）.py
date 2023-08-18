import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

# 1 부터 n까지의 자연수 중에서 m개를 고른 수열
# 같은수 여러번 가능
# 비내림차순 (오름차순)

n, m = map(int, input().split())

combi = combinations_with_replacement(list(range(1, n+1)), m)

for comb in combi:
    for i in range(len(comb)):
        print(comb[i], end=' ')
    print()