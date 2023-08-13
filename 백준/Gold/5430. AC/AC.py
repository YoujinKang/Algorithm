import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ftn_list = input().rstrip()
    n = int(input())  # 0 <= n <= 100,000
    arr = deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        arr = []

    flag = 0  # 뒤집기 없음
    for ftn in ftn_list:
        if ftn == 'R':
            flag += 1  # 뒤집기 개수 셈
        else:  # ftn == 'D'
            if len(arr) == 0:
                print('error')
                break
            else:
                if flag % 2 == 0:  # 여러번 뒤집어서 다시 원래 상태라면
                    arr.popleft()
                else:  # 원래 상태에서 뒤집힌 상태
                    arr.pop()

    else:  # n != 0
        if flag % 2 == 0:  # 원래 상태
            print("[" + ','.join(arr) + "]")
        else:  # 뒤집힌 상태
            arr.reverse()
            print("[" + ','.join(arr) + "]")

