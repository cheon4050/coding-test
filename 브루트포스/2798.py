n, m = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or j == k:
                continue
            temp = data[i] + data[j] + data[k]
            if temp > cnt and temp <= m:
                cnt = temp
print(cnt)
