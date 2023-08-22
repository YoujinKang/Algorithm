import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())  # 집의 수 4
houses = list(map(int, input().split()))  # 1 5 7 9
houses.sort()

print(houses[(n-1)//2])