import sys
input = sys.stdin.readline

# 1 / 1, 2 / 3, 2, 1 / 1, 2, 3, 4 / 5, 4, 3, 2, 1, / ...
# 1 / 2, 1 / 1, 2, 3 / 4, 3, 2, 1 / 1, 2, 3, 4, 5, / ...

x = int(input())
cnt, need = 0, 0
for i in range(1, 10000001):
    cnt += i
    if cnt == x:
        need = 0
        break
    elif cnt > x:  # 10 >= 8
        cnt -= i  # cnt = 6
        need = x - cnt  # need = 2, i = 4
        break

if need == 0:
    nominator = str(i) # 4
    denominator = str(1)
else:  # need > 0
    nominator = str(need)
    denominator = str(i - need + 1)

if i % 2 == 0:
    print(f"{nominator}/{denominator}")
else:
    print(f"{denominator}/{nominator}")