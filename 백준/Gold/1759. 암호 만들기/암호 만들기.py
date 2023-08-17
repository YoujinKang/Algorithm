import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
possible = sorted(list(map(str, input().split())))

vow = ['a', 'e', 'i', 'o', 'u']
keys = []
combi = combinations(possible, l)
for comb in combi:
    new_comb = "".join(sorted(comb))
    num_vow = sum(new_comb.count(v) for v in vow)
    num_con = 0
    for c in new_comb:
        if c not in vow:
            num_con += 1
    if num_vow >= 1 and num_con >= 2:
        keys.append(new_comb)

keys = sorted(keys)
for key in keys:
    print(key)