import sys
import heapq
input = sys.stdin.readline
INF = int(1E9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [INF] * (n + 1)
distance[x] = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n2 in graph[node]:
            cost = distance[node] + 1
            if cost < distance[n2]:
                distance[n2] = cost
                heapq.heappush(q, (cost, n2))

dijkstra(x)
if k not in distance:
    print(-1)
else:
    for i in range(1, len(distance)):
        if distance[i] == k:
            print(i)