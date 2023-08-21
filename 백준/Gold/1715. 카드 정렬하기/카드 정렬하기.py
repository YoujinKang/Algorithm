import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
# 가장 작은값이 먼저 나오도록

q = PriorityQueue()
for _ in range(n):
    q.put(int(input()))  # 4 5 6 7

tot_cnt = 0

while q.qsize() != 1:
    val1 = q.get()  # 4 # 6 # 9
    val2 = q.get()  # 5 # 7 # 13
    tot_cnt += (val1 + val2)  # 9 # 13 # 22
    q.put(val1+val2)  # q = [6, 7, 9] # [9, 13] # [22]

print(tot_cnt)