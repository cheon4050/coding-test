m = input()
n = 0
result = ""
arr = ""
while n < len(m):
    if m[n] == "<":
        result += arr[::-1]
        arr = ""
        while m[n] != ">":
            result += m[n]
            n += 1
        result += m[n]
        n += 1
    elif m[n] == " ":
        result += arr[::-1]
        arr = ""
        result += " "
        n += 1
    else:
        arr += m[n]
        n += 1
result += arr[::-1]

print(result)
