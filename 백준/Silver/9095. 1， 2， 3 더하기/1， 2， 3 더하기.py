import sys
input = sys.stdin.readline

t = int(input())

d = [0] * 11
d[1] = 1
d[2] = 1 + d[1]  # : 2+0, 1만들기 +1
d[3] = 1 + d[2] + d[1]  # : 3+0, 2만들기 + 1, 1만들기 + 2
# d[4] = d[3] + d[2] + d[1] + : 3만들기 +1, 2만들기 +2, 1만들기 + 3
# d[5] = : 4만들기 +1, 3만들기 +2, 2만들기 +3
for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for _ in range(t):
    n = int(input())
    print(d[n])
