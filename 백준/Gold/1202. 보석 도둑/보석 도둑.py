import sys
import heapq
input = sys.stdin.readline

# 보석 n개, 무게 m, 가격 v, 가방 k개, 최대무게 c

n, k = map(int, input().split())  # 3 2
gems = []
for _ in range(n):
    heapq.heappush(gems, list(map(int, input().split())))  # [(1 65), (5 23), (2 99)]
bags = [int(input()) for _ in range(k)]  # [10, 2]
bags.sort()

value = 0
temp = []
for bag in bags:
    while gems and gems[0][0] <= bag:  # 가장 가벼운 보석부터 현재 가방에 들어갈 수 있는 보석만 temp 힙에 넣음
        m, v = heapq.heappop(gems)
        heapq.heappush(temp, -v)

    if temp:  # temp 힙에서 가장 큰 값을 value에 넣음 bag의 수 만큼만 돌아감
        value += -heapq.heappop(temp)

print(value)
