import sys
from heapq import heapify
from heapq import heappop
from heapq import heappush

n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    heap = list(map(int, sys.stdin.readline().split(" ")))
    heapify(heap)
    result = 0
    while len(heap) >= 2:
        cnt = heappop(heap) + heappop(heap)
        result += cnt
        heappush(heap, cnt)
    print(result)
