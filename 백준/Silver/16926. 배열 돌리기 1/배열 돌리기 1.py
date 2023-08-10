import sys 
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 배열의 크기 n * m, 회전 수 r
a = [list(map(int, input().split())) for _ in range(n)]

b = [[0] * m for _ in range(n)]
q = deque()

h = min(n, m) // 2

for i in range(h):
    # 초기화
    q.clear()
    # q 에 시계 방향으로 저장
    q.extend(a[i][i:m-i])
    q.extend([row[m-i-1] for row in a[i+1:n-i-1]])
    q.extend(a[n-i-1][i:m-i][::-1])
    q.extend([row[i] for row in a[i+1:n-i-1]][::-1])

    # r만큼 회전 -> 각 값들이 r만큼 인덱스 앞으로 밀림
    q.rotate(-r)

    # 위 row
    for j in range(i, m-i):
        b[i][j] = q.popleft()
    # 오른쪽 column
    for j in range(i+1, n-i-1):
        b[j][m-i-1] = q.popleft()
    # 아래 row
    for j in range(m-i-1, i-1, -1):
        b[n-i-1][j] = q.popleft()
    # 왼쪽 column
    for j in range(n-i-2, i, -1):
        b[j][i] = q.popleft()

for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=" ")
    print("")