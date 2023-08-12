import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) 
    q = deque(map(int, input().split()))
    q = deque([(p, i) for i, p in enumerate(q)])

    cnt = 0
    while q:
        if q[0][0] == max(q, key=lambda x: x[0])[0]:  # 처음에 저장된 값이 maximum priority 일 때
            cnt += 1  # 프린트물 출력
            if q[0][1] == m:  # 확인하고자 하는 인덱스면
                print(cnt)
                break
            else:
                q.popleft()
        else:  # 처음에 저장된 값이 maximum priority가 아니면 빼서 다시 q의 맨 뒤에 넣음
            p, i = q.popleft()
            q.append((p, i))

