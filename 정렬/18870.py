import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
arr2 = []
for i in range(len(arr)):
    arr2.append([arr[i], i])

arr3 = sorted(arr2, key=lambda x: x[0])
cnt = 0
for i in range(len(arr3)):
    try:
        if arr3[i][0] != arr3[i + 1][0]:
            arr3[i][0] = cnt
            cnt += 1
        else:
            arr3[i][0] = cnt
    except:
        arr3[i][0] = cnt
arr3 = sorted(arr3, key=lambda x: x[1])
for i in range(len(arr3)):
    print(arr3[i][0], end=" ")
