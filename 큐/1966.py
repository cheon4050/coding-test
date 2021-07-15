S = int(input())
result = []


def solution(priorities, location):
    answer = 0
    while len(priorities) > 1:
        num = priorities.pop(0)
        nummax = max(priorities)
        if num < nummax:
            priorities.append(num)
            location = (location - 1) % len(priorities)
        else:
            answer += 1
            if location == 0:
                return answer
            else:
                location = (location - 1) % len(priorities)

    return answer + 1


for _ in range(S):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result.append(solution(arr, m))

for i in range(len(result)):
    print(result[i])
