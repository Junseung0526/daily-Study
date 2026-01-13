import heapq

def max_heap_test():
    nums = [4, 1, 7, 3, 8, 5]
    max_heap = []

    # 최대 힙 구현 (마이너스 부호를 붙여서 푸시)
    for n in nums:
        heapq.heappush(max_heap, -n)

    print("내부적인 힙 상태(음수):",max_heap)


    # 뺄 때 다시 마이너스를 붙여서 원래 숫자로 복구
    result = []
    while max_heap:
        result.append(-heapq.heappop(max_heap))

    return result

print(max_heap_test())