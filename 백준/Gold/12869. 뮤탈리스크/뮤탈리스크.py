import sys 
from itertools import permutations

n = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:
    scv += [0]

max_scv = max(scv)

# 최소 횟수를 기록
# 각 scv가 9, 3, 1의 공격을 번갈아 받는 것을 모두 고려하여 3차원 리스트 만듦
# d[scv1체력][scv2체력][scv3체력] 을 저장. d[0][0][0] 에 있는 값을 읽고자 함
d = [[[61] * (max_scv + 1) for _ in range(max_scv + 1)] for _ in range(max_scv + 1)]
ans = 61

def attack(i, j, k, cnt):
    global ans
    if i <= 0 and j <= 0 and k <= 0:
        if ans > cnt:
            ans = cnt
            return 
        
    i = 0 if i <= 0 else i
    j = 0 if j <= 0 else j
    k = 0 if k <= 0 else k

    # 이미 저장된 값이 cnt보다 작으면 작은 값으로 내버려둠
    if d[i][j][k] <= cnt and d[i][j][k] != 0:
        return
    
    d[i][j][k] = cnt

    for x in permutations([9, 3, 1], 3):
        attack(i - x[0], j - x[1], k - x[2], cnt + 1)

attack(scv[0], scv[1], scv[2], 0)
print(ans)