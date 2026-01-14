import heapq
import sys

# 무한대
INF = int(1e9)


def dijkstra(start, graph, n):
    distance = [INF] * (n + 1)
    queue = []

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance


n = 3
graph = [[] for _ in range(n + 1)]
graph[1].append((2, 2))  # 1번에서 2번으로 가는 비용 2
graph[1].append((3, 5))  # 1번에서 3번으로 가는 비용 5
graph[2].append((3, 1))  # 2번에서 3번으로 가는 비용 1

print(f"1번 노드에서 각 노드까지의 최단 거리: {dijkstra(1, graph, n)[1:]}")