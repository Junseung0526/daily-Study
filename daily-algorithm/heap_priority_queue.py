import heapq


def head_sort_test():
    nums = [4, 1, 7, 3, 8, 5]
    heap = []

    # 모든 숫자 힙에 넣기
    for n in nums:
        # 데이터를 넣는다. (Enqueue)
        heapq.heappush(heap, n)

    # 힙에서 하나씩 빼서 정렬시키기
    sorted_nums = []

    # 가장 작은(우선순위 높은) 것부터 뺀다. (Dequeue)
    while heap:
        sorted_nums.append(heapq.heappop(heap))

    return sorted_nums


# 실행 결과 확인
print(head_sort_test())
