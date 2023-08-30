import sys
import heapq
input = sys.stdin.readline
INF = int(1E9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, f, t = map(int, input().split())
    graph[s].append((f, t))

def dijkstra(start, n):
    distance = [INF] * (n + 1)
    distance[0], distance[start] = 0, 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n, c in graph[node]:
            cost = distance[node] + c
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))
    return distance

distance_cost = [0] * (n + 1)
distance_from_x = dijkstra(x, n)
for i in range(1, n + 1):
    if i == x:
        continue
    distance = dijkstra(i, n)
    distance_cost[i] = distance[x] + distance_from_x[i]

print(max(distance_cost))
