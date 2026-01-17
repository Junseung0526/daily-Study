from collections import deque


def topology_sort(n, edges):
    result = []
    queue = deque()
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]


    # 진입 차수 그래프 구성
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌 때까지 반복
    while queue:
        now = queue.popleft()
        result.append(now)

        # 해당 원소 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 삽입
            if indegree[i] == 0:
                queue.append(i)

    return result


# 테스트 케이스
n = 3
edges = [(1, 2), (2, 3)]


# 출력: [1, 2, 3]
print(f"공부 순서: {topology_sort(n, edges)}")
