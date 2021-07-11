n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))


def binary_search(array, target, start, end):
    mid = int((start + end) / 2)
    if start > end:
        print(0, end=" ")
    elif target < array[mid]:
        binary_search(array, target, start, mid - 1)
    elif target > array[mid]:
        binary_search(array, target, mid + 1, end)
    else:
        print(1, end=" ")


for i in arr2:
    binary_search(arr, i, 0, len(arr) - 1)
