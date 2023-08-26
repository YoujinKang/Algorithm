import sys
import heapq
input = sys.stdin.readline

# 3월 1일부터 11월 30일까지 최소 한가지 이상. 꽃의 개수는 최소한
n = int(input())
dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 1월 1일: 1, 2월 1일: 31 + 1, 3월 1일: 31 + 28 + 1, 4월 1일: 31 + 28 + 31 + 1, 5월 1일: 31 + 28 + 31 + 30 + 1
flower_data = []
for _ in range(n):
    s1, s2, f1, f2 = map(int, input().split())
    s_date = sum(dates[:s1]) + s2
    f_date = sum(dates[:f1]) + f2
    heapq.heappush(flower_data, (s_date, f_date))  # s_date가 가장 작은 요소가 flower_data[0]으로 감

start_date = sum(dates[:3]) + 1
final_date = sum(dates[:11]) + 30  

steps = start_date
num_flowers = 0
while flower_data:
    if start_date > final_date or start_date < flower_data[0][0]:
        break
    for _ in range(len(flower_data)):
        if start_date >= flower_data[0][0]:
            if steps < flower_data[0][1]:  # 이전에 심는다고 가정할 때 갈 수 있는 기간보다 더 오래 갈 수 있을 때
                steps = flower_data[0][1]
            heapq.heappop(flower_data)
        else:
            break
    start_date = steps
    num_flowers += 1

if start_date <= final_date: 
    print(0)
else:
    print(num_flowers)
