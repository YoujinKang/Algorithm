import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

transform = 0
# t에서 하나씩 빼면서 s를 만들 수 있는지 확인
while t:
    if t[-1] == "A":
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t.reverse()
    if s == t:
        transform = 1
        break

print(transform)