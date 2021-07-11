import sys

res = 0


def tam(data, target, start, end):
    global res
    result = 0
    if start <= end:
        mid = (start + end) // 2
        for i in data:
            if i > mid:
                result += i - mid
        if result < target:
            tam(data, target, start, mid - 1)
        else:
            res = mid
            tam(data, target, mid + 1, end)


n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(data)
data.sort(reverse=True)
tam(data, m, start, end)
print(res)
