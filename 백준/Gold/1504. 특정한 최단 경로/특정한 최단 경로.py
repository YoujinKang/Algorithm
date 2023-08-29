import sys
import heapq
input = sys.stdin.readline
INF = int(1E9)

n, e = map(int, input().split())
graph = [[] for i in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, final, n):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n, c in graph[node]:
            cost = dist + c
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))
    return distance[final]

dist11 = dijkstra(1, v1, n)
dist12 = dijkstra(1, v2, n)
dist21 = dijkstra(v1, v2, n)
dist22 = dijkstra(v2, v1, n)
dist31 = dijkstra(v2, n, n)
dist32 = dijkstra(v1, n, n)
# v1을 먼저 거치는 경우와 v2를 먼저 거치는 경우로 구별해서 minimum 저장
dist = min(dist11 + dist21 + dist31, dist12 + dist22 + dist32)
if dist >= INF:
    print(-1)
else:
    print(dist)


