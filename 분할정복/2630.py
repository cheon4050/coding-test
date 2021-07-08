import sys

sys.setrecursionlimit(10 ** 9)
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


def solution(arr, cnt, garo, sero, result):
    temp = arr[garo][sero]
    for i in range(cnt):
        stop = False
        for j in range(cnt):
            if not temp == arr[garo + i][sero + j]:
                solution(arr, cnt / 2, garo, sero)
                solution(arr, cnt / 2, garo + cnt / 2, sero)
                solution(arr, cnt / 2, garo, sero + cnt / 2)
                solution(arr, cnt / 2, garo + cnt / 2, sero + cnt / 2)
                stop = True
                break
        if stop == True:
            break
    else:
        if temp == 0:
            result[0] += 1
        else:
            result[1] += 1


result = [0, 0]
solution(arr, n, 0, 0, result)
print(result[0])
print(result[1])
