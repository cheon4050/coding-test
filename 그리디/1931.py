import sys

n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort()

start = data[0][0]
end = data[0][1]
result = 1
for s, e in data[1:]:
    if end <= s:
        start = s
        end = e
        result += 1
    elif end > e:
        end = e

print(result)
