n = int(input())
arr = [0 for _ in range(n + 1)]


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif arr[n] != 0:
        return arr[n]
    else:
        arr[n] = fibo(n - 1) + fibo(n - 2)
        return arr[n]


print(fibo(n))
