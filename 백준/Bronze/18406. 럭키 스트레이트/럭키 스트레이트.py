import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))  # 점수. 자릿수는 항상 짝수

front_sum = sum(n[:len(n) // 2])
back_sum = sum(n[len(n)//2:])

if front_sum == back_sum:
    print("LUCKY")
else:
    print("READY")