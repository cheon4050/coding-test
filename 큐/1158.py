n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]
arr2 = []
index = k - 1
for i in range(n):
    arr2.append(str(arr.pop(index)))
    if i == n - 1:
        break
    index = (index + k - 1) % len(arr)
print("<" + ", ".join(arr2) + ">")
