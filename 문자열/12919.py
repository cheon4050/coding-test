S = input()
T = input()
arr = []
arr2 = []


def solution(S):
    global T
    if S == T:
        arr.append(1)
        return
    elif S not in T and S[::-1] not in T:
        arr.append(0)
        return
    else:
        solution(S + "A")
        solution((S + "B")[::-1])


solution(S)
print(max(arr))
