import heapq


def prim(start_node, n, graph):
    visited = [False] * (n + 1)
    pq = [(0, start_node)]
    total_weight = 0
    count = 0

    while pq:
        weight, now = heapq.heappop(pq)

        if visited[now]:
            continue

        visited[now] = True
        total_weight += weight
        count += 1

        if count == n: break

        for next_node, next_weight in graph[now]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_weight, next_node))

    return total_weight


# 테스트 케이스
n = 3
graph = [[] for _ in range(n + 1)]
graph[1].append((2, 10))  # 1-2 비용 10
graph[2].append((1, 10))
graph[2].append((3, 20))  # 2-3 비용 20
graph[3].append((2, 20))
graph[1].append((3, 5))  # 1-3 비용 5
graph[3].append((1, 5))

print(f"최소 신장 트리 총 비용: {prim(1, n, graph)}")  # 결과: 15 (1-3, 1-2 연결)
