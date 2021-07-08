n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))
result = ""


def solution(n, row, col):
    global result
    for i in range(n):
        for j in range(n):
            if arr[row + i][col + j] != arr[row][col]:
                result += "("
                solution(int(n / 2), row, col)
                solution(int(n / 2), row, col + int(n / 2))
                solution(int(n / 2), row + int(n / 2), col)
                solution(int(n / 2), row + int(n / 2), col + int(n / 2))
                result += ")"
                return
    else:
        result += str(arr[row][col])


solution(n, 0, 0)
print(result)
