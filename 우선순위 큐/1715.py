import heapq
import sys

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))
cnt = 0
while len(heap) >= 2:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    cnt += a + b
    heapq.heappush(heap, a + b)
print(cnt)
