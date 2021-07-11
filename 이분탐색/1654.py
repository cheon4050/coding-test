import sys

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
maxnumber = max(arr)

result = 0


def binary_search(array, target, start, end):
    global result
    mid = int((start + end) / 2)
    sum = 0
    if mid == 0:
        mid = 1
    for i in array:
        sum += i // mid

    if start > end:
        return
    elif sum < target:
        binary_search(array, target, start, mid - 1)
    elif sum >= target:
        result = max(result, mid)
        binary_search(array, target, mid + 1, end)


binary_search(arr, k, 0, maxnumber)

print(result)
