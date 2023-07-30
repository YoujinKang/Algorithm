import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

d = [1] * (n)

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + 1)


print(max(d))

order = max(d)
arr = []
for i in range(n-1, -1, -1):
    if d[i] == order:
        arr.append(a[i])
        order -= 1
        
arr.reverse()
for i in arr:
    print(i, end=' ')
