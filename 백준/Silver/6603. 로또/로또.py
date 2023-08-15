import sys
from itertools import combinations
input = sys.stdin.readline

# 1부터 49까지 중 6개 고르는 로또
# k개의 수를 골라 집합 S를 만든 다음, 그 수만 가지고 번호를 선택하는 것
# 예) k=8, S={1, 2, 3, 5, 8, 13, 21, 34} 인 경우, 이 집합 S에서 6개의 수를 고르는 경우의 수는 28개

while True:
    data = list(map(int, input().split()))
    if len(data) == 1 and data[0] == 0:
        break

    k, s = data[0], sorted(data[1:])
    combi = combinations(s, 6)
    for value in combi:
        temp = list(map(str, value))
        print(" ".join(temp))
    print()