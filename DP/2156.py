import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr2 = [[0, 0] for _ in range(n + 1)]


def solution(i):
    cnt = 1
    while i >= 0:
        if arr2[i + 1][1] == 2:
            arr2[i][0] = max(
                arr[i] + arr[i + 1] + arr2[i + 3][0],
                arr[i] + arr2[i + 2][0],
                arr2[i + 1][0],
            )
            if arr2[i][0] == arr2[i + 1][0]:
                arr2[i][1] = 0
                cnt = 1
                i -= 1
            elif arr2[i][0] == arr[i] + arr2[i + 2][0]:
                arr2[i][1] = 1
                cnt = 2
                i -= 1
            else:
                arr2[i][1] = 2
                cnt = 3
                i -= 1
        else:
            arr2[i] = [arr[i] + arr2[i + 1][0], cnt]
            cnt += 1
            i -= 1


solution(n - 1)
print(arr2[0][0])
