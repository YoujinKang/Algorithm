import sys
input = sys.stdin.readline

# d(n) = n + n의 각 자리수의 합. n을 생성자라고 할 때, 생성자가 없는 숫자를 셀프 넘버라고 함
# 1의 자리: n % 10, 10의 자리: (n // 10) % 10, 100의 자리: (n // 100) % 10

d = [0] * 10001
for i in range(1, 10001):
    constructor = i
    for j in range(len(str(i))):
        constructor += ((i // (10 ** j)) % 10)
        if constructor > 10000:
            break
    if constructor <= 10000:
        d[constructor] = 1

for k in range(1, 10001):
    if d[k] == 0:
        print(k)