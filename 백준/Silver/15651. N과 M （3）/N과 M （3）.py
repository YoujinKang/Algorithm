import sys
from itertools import product
input = sys.stdin.readline

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러번 골라도 된다.
n, m = map(int, input().split())

combi = product(list(range(1, n+1)), repeat=m)
for comb in combi:
    for j in range(len(comb)):
        print(comb[j], end=" ")
    print()