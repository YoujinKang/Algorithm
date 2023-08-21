import sys
import time
input = sys.stdin.readline

n = int(input())  # 4 <= n <= 20
s = [list(map(int, input().split())) for _ in range(n)]
start_mem = [0] * n  # 스타트 그룹 멤버 확인하는 용도

min_diff = sys.maxsize

def check_min():
    global min_diff
    start, link = 0, 0
    for i in range(n):
        for j in range(i+1, n):
            if start_mem[i] and start_mem[j]:  # 둘 다 스타트 멤버면
                start += s[i][j] + s[j][i]
            elif not start_mem[i] and not start_mem[j]:  # 둘 다 링크 멤버면
                link += s[i][j] + s[j][i]
    min_diff = min(min_diff, abs(start - link))
    return

def backtracking(i):
    if i == n:
        check_min()
        return
    start_mem[i] = 1
    backtracking(i + 1)
    if i == 0:  # 0번째 사람이 0인 케이스부터 다시 시작하면, 링크 <-> 스타트의 교환일 뿐이므로 계산안함
        return
    start_mem[i] = 0
    backtracking(i + 1)
    return


backtracking(0)
print(min_diff)