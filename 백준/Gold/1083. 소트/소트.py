import sys
input = sys.stdin.readline

n = int(input()) 
a = list(map(int, input().split())) 
s = int(input()) 

id = 0
while s > 0:
    max_idx = a[id:id + s+1].index(max(a[id:id + s+1]))
    for i in range(id+max_idx, id, -1):
        a[i], a[i-1] = a[i-1], a[i]
        s -= 1
        if s == 0:
            break
    id += 1
    if id >= n - 1:
        break


for x in a:
    print(x, end=' ')