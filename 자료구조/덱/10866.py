import sys
from collections import deque

n = int(input())
Deque = deque()
for i in range(n):
    answer = sys.stdin.readline().rstrip()
    if answer[:10] == "push_front":
        Deque.appendleft(int(answer.split()[1]))
    elif answer[:9] == "push_back":
        Deque.append(int(answer.split()[1]))
    elif answer == "pop_front":
        if not Deque:
            print(-1)
        else:
            print(Deque.popleft())
    elif answer == "pop_back":
        if not Deque:
            print(-1)
        else:
            print(Deque.pop())
    elif answer == "size":
        print(len(Deque))
    elif answer == "empty":
        if not Deque:
            print(1)
        else:
            print(0)
    elif answer == "front":
        if not Deque:
            print(-1)
        else:
            print(Deque[0])
    elif answer == "back":
        if not Deque:
            print(-1)
        else:
            print(Deque[-1])
