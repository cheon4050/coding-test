n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr2 = [0 for _ in range(n + 1)]


def DP(i):
    global n
    if i < 0:
        return
    if arr[i][0] + i > n:
        arr2[i] = arr2[i + 1]
        DP(i - 1)
    else:
        arr2[i] = max(arr2[i + 1], arr[i][1] + arr2[i + arr[i][0]])
        DP(i - 1)


DP(n - 1)
print(arr2[0])
