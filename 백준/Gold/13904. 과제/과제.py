import sys
import heapq
input = sys.stdin.readline

n = int(input())
tasks = []

date = 0  # 가장 늦은 deadline 저장
for _ in range(n):
    d, w = map(int, input().split())  # deadline, score
    heapq.heappush(tasks, (-w, d))  # score 높은 순  & [(-60, 4), (-50, 2), (-40, 4), (-30, 3), (-10, 4), (-5, 6)]
    date = max(date, d)  # 6

works = [0] * (date + 1)

tot_score = 0
while tasks:
    w, d = heapq.heappop(tasks)  # (-60, 4) -> 4일차에 수행하면 좋음  # (-50, 2) -> 2일차에 수행  # (-40, 4) -> 4일차가 안됨. 3일차
    for i in range(d, 0, -1):  # 4, 3, 2, 1  # 2, 1  # 4, 3, 2, 1
        if works[i] == 0:
            works[i] = 1  # work[4] = 1  # work[2] = 1  # work[4] 가 이미 1 이므로 work[3] = 1
            tot_score -= w  # tot_score = 60  # tot_score = 110
            break

print(tot_score)