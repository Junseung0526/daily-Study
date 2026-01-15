def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = 3, 3
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

edges = []
result = 0

edges.append((10, 1, 2))
edges.append((20, 2, 3))
edges.append((5, 1, 3))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(f"최소 신장 트리 총 비용: {result}")  # 출력 결과: 15
