import sys
input = sys.stdin.readline

n = int(input())
scale = list(map(int, input().split()))
scale.sort()  # [1, 1, 2, 3, 6, 7, 30]

start = 0
end = 0
for i in scale:
    if start + i <= end + 1:  # 1 <= 1  # 1 <= 2
        end += i  # 1 -> [0, 1]  # 2 -> [0, 2]

print(end+1)