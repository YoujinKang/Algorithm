import sys
import heapq
input = sys.stdin.readline
INF = int(1E9)

n = int(input())  # 땅 후보의 개수
a, b, c = map(int, input().split())
m = int(input())  # 에지의 수
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    d, e, l = map(int, input().split())
    graph[d].append((e, l))
    graph[e].append((d, l))

def dijkstra(start, n):
    q = []
    distance = [INF] * (n + 1)
    distance[0], distance[start] = 0, 0
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

dist_a = dijkstra(a, n)
dist_b = dijkstra(b, n)
dist_c = dijkstra(c, n)

max_size = 0
result = 0
for i in range(1, n + 1):
    min_val = min(dist_a[i], dist_b[i], dist_c[i])
    if max_size < min_val:
        max_size = min_val
        result = i
print(result)