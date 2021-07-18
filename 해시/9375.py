import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    hash = {}
    cnt = 0
    for i in range(num):
        name, ctype = sys.stdin.readline().split()
        if ctype not in hash:
            hash[ctype] = 1
        else:
            hash[ctype] += 1
    result = 1
    for i in hash:
        result *= hash[i] + 1
    result -= 1
    print(result)
