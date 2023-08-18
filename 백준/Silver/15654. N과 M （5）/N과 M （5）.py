import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

combi = permutations(array, m)
for comb in combi:
    for j in range(len(comb)):
        print(comb[j], end=" ")
    print()