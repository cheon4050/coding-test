import heapq
import sys

n = int(input())
arr = []
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split(" "))
    arr.append((s, t))
arr.sort()
heap = [0]
for i in range(len(arr)):
    s, t = arr[i]
    if heap[0] <= s:
        heapq.heappop(heap)
        heapq.heappush(heap, t)
    else:
        heapq.heappush(heap, t)
print(len(heap))
