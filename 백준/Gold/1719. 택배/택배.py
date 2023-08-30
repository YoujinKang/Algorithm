import sys
import heapq
input = sys.stdin.readline
INF = int(1E9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    visited[a] = []
    visited[b] = []

def dijkstra(start, n, visit):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start, []))
    while q:
        dist, node, path = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n2, c in graph[node]:
            cost = distance[node] + c
            if cost < distance[n2]:
                distance[n2] = cost
                new_path = path + [n2]
                visit[n2] = new_path
                heapq.heappush(q, (cost, n2, new_path))
    return visit


for i in range(1, n + 1):
    visit = dijkstra(i, n, visited)
    for j in range(1, n + 1):
        if i == j:
            print("-", end=' ')
        else:
            print(visit[j][0], end=' ')
    print()