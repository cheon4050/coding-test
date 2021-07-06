n = int(input())
arr = [[" " for _ in range((n*4)-3)] for i in range((n*4)-3)]


def star(n, k, arr):
    temp = (n*4)-3
    for i in range(temp):
        arr[(k-n)*2][i+((k-n)*2)] = "*"
        arr[i+((k-n)*2)][(k-n)*2] = "*"
        arr[temp-1+((k-n)*2)][i+((k-n)*2)] = "*"
        arr[i+((k-n)*2)][temp-1+((k-n)*2)] = "*"

    if n != 1:
        star(n-1, k, arr)


star(n, n, arr)
for i in arr:
    print("".join(i))
