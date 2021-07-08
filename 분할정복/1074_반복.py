n, r, c = map(int, input().split())
result = 0


def solution(n, row, col):
    global result
    stop = True
    while stop:
        if n <= 1:
            for i in range(2):
                for j in range(2):
                    if row + i == r and col + j == c:
                        print(result)
                        stop = False
                    else:
                        result += 1
        elif row + int(n / 2) <= r and col + int(n / 2) <= c:
            result += int(((n / 2) ** 2) * 3)
            row = row + int(n / 2)
            col = col + int(n / 2)
            n = int(n / 2)
        elif row + int(n / 2) <= r:
            result += int(((n / 2) ** 2) * 2)
            row = row + int(n / 2)
            n = int(n / 2)
        elif col + int(n / 2) <= c:
            result += int(((n / 2) ** 2))
            col = col + int(n / 2)
            n = int(n / 2)
        elif n >= 2:
            n = int(n / 2)


solution(2 ** n, 0, 0)
