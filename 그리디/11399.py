n = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = 0
for i in range(1, n + 1):
    result += sum(arr[:i])

print(result)
