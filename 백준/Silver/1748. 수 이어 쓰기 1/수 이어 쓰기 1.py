import sys
input = sys.stdin.readline

n = int(input())

# 1 ~ 9 까지 = 1 * (9 - 1 + 1)
# 10 ~ 99 까지 = 2 * (99 - 10 + 1)
# 100 ~ 999 까지 = 3 * (999 - 100 + 1)

# n = 43591 이라고 한다면 len(str(n)) = 5
# 10000 ~ 43591 -> 5 * (n - 10000 + 1)

result = 0
for i in range(1, len(str(n))):
    result += i * (int(str(9) * i) - (10 ** (i-1)) + 1)

result += len(str(n)) * (n - (10 ** (len(str(n)) - 1)) + 1)

print(result)