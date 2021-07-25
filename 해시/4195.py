import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(number, parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a
        number[a] += number[b]


case = int(input())
for _ in range(case):
    e = int(sys.stdin.readline())
    parent = {}
    number = {}
    for i in range(e):
        a, b = sys.stdin.readline().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union_parent(number, parent, a, b)
        print(number[find_parent(a)])
