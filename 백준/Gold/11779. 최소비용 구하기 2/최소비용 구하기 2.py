import sys
import heapq
input = sys.stdin.readline
INF = int(1E9)

n = int(input())
m = int(input())
graph = [{} for _ in range(n + 1)]
visited = {}
for _ in range(m):
    s, f, c = map(int, input().split())
    if f not in graph[s].keys():
        graph[s][f] = c
    else:
        graph[s][f] = min(graph[s][f], c)
    visited[s] = []

start, final = map(int, input().split())
distance = [INF] * (n + 1)
distance[start] = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, [start]))  # distance, node, path
    while q:
        dist, node, path = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n, c in graph[node].items():
            cost = distance[node] + c  # start에서 node를 찍고 n까지 가는 거리
            if cost < distance[n]:  # start에서 n까지 저장된 비용보다 비용이 적으면
                distance[n] = cost
                new_path = path + [n]
                visited[n] = new_path
                heapq.heappush(q, (cost, n, new_path))

dijkstra(start)
path = [str(x) for x in visited[final]]
print(distance[final])
print(len(path))
print(" ".join(path))