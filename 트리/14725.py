import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    temp = list(sys.stdin.readline().rstrip().split())
    temp = temp[1:]
    arr.append(temp)


def solution(arr, cnt):
    if not arr:
        return
    if len(arr[0]) == 0:
        return
    arr.sort(key=lambda x: x[0])
    rlwns = len(arr)
    rlwns2 = arr[0][0]
    for i in range(len(arr)):
        if not arr[i]:
            continue
        if arr[i][0] != rlwns2:
            rlwns = i
            break
        arr[i] = arr[i][1:]
    print("--" * cnt + rlwns2)
    solution(arr[:rlwns], cnt + 1)
    solution(arr[rlwns:], cnt)


solution(arr, 0)
