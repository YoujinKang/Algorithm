import heapq
import sys
input = sys.stdin.readline

def myPrecious(jewel, sack):
    total = 0
    precious = []
    for bound in sack:
        while jewel and jewel[0][0] <= bound:
            heapq.heappush(precious, -heapq.heappop(jewel)[1])

        if precious:
            total -= heapq.heappop(precious)
        elif not jewel:
            break
    return total

###

n, k = map(int, input().split())

jewel = []
for _ in range(n):
    heapq.heappush(jewel, list(map(int, input().split()))) # w, v


sack = []
for _ in range(k):
    sack.append(int(input()))
sack.sort()

print(myPrecious(jewel, sack))