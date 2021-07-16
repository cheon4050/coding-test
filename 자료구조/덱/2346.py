n = int(input())

arrtemp = list(map(int, input().split()))
arr = []
for i in enumerate(arrtemp):
    arr.append(i)
index = 0
result = []
for i in range(n):
    cnt, move = arr.pop(index)
    if not arr:
        result.append(str(cnt + 1))
        break
    if move < 0:
        index = (index + move) % len(arr)
    else:
        index = (index + move - 1) % len(arr)
    result.append(str(cnt + 1))
print(" ".join(result))
