import sys
import heapq
input = sys.stdin.readline

# s_i 에 시작해서 t_i에 끝나는 i 수업이 총 n개.
# 최소 강의실

n = int(input())  # 3
lectures = [list(map(int, input().split())) for _ in range(n)]
lectures.sort()

# 끝나는 시간 저장
prev_lecture = []
heapq.heappush(prev_lecture, lectures[0][1])

for i in range(1, n):
    if (lectures[i][0] < prev_lecture[0]):  # 다른 강의실 필요
        heapq.heappush(prev_lecture, lectures[i][1])
    else:  # 현재 강의실 업데이트
        heapq.heappop(prev_lecture) # 현재 강의실 업데이트
        heapq.heappush(prev_lecture, lectures[i][1])

print(len(prev_lecture))