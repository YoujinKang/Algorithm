import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]

# 산술평균
print(int(round(sum(data) / len(data), 0)))
# 중앙값
mid = len(data) // 2
new_data = sorted(data)
print(new_data[mid])
# 최빈값
most_common = Counter(new_data).most_common()
if len(new_data) > 2:
    if most_common[1][1] == most_common[0][1]:
        print(most_common[1][0])
    else:
        print(most_common[0][0])
else:
    print(most_common[0][0])
# 범위
print(new_data[-1] - new_data[0])
