n, r, c = map(int, input().split())

result = 0


def solution(n, row, col):
    global result
    if n <= 1:
        for i in range(2):
            for j in range(2):
                if row + i == r and col + j == c:
                    print(result)
                    return
                else:
                    result += 1
    if row + int(n / 2) <= r and col + int(n / 2) <= c:
        result += int(((n / 2) ** 2) * 3)
        solution(int(n / 2), row + int(n / 2), col + int(n / 2))
    elif row + int(n / 2) <= r:
        result += int(((n / 2) ** 2) * 2)
        solution(int(n / 2), row + int(n / 2), col)
    elif col + int(n / 2) <= c:
        result += int(((n / 2) ** 2))
        solution(int(n / 2), row, col + int(n / 2))
    else:
        solution(int(n / 2), row, col)


solution(2 ** n, 0, 0)
