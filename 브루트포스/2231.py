n = int(input())
for i in range(1, n):
    stri = str(i)
    result = i
    for k in range(len(stri)):
        result += int(stri[k])
    if result == n:
        print(i)
        break
else:
    print(0)
