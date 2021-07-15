data = input()
stack = []
result = 0
arr = []
cnt = 0
for i in data:
    if i == "(" or i == "[":
        cnt = 0
        stack.append(i)
    elif i == ")":
        if not stack:
            break
        elif stack[-1] == "(":
            temp = 1
            if cnt == 0:
                for j in stack:
                    if j == "(":
                        temp *= 2
                    else:
                        temp *= 3
                arr.append(str(temp))
            cnt = 1
            stack.pop()
        else:
            break
    elif i == "]":
        if not stack:
            break
        elif stack[-1] == "[":
            temp = 1
            if cnt == 0:
                for j in stack:
                    if j == "(":
                        temp *= 2
                    else:
                        temp *= 3
                arr.append(str(temp))
            cnt = 1
            stack.pop()
        else:
            break
else:
    result = eval("+".join(arr))
print(result)
print(eval("+".join(["1"])))
