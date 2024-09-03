import sys
from collections import deque

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    tree_parents = {i+1:-1 for i in range(N)}
    tree_children = {i+1:[] for i in range(N)}

    for _ in range(N-1):
        a,b = map(int, sys.stdin.readline().split())
        tree_parents[b] = a
        tree_children[a].append(b)

    n1,n2 = map(int, sys.stdin.readline().split())

    n1_parents = set([n1])
    while tree_parents[n1] != -1:
        n1 = tree_parents[n1]
        n1_parents.add(tree_parents[n1])

    n2_parents = set([n2])
    while tree_parents[n2] != -1:
        n2 = tree_parents[n2]
        n2_parents.add(tree_parents[n2])

    q = deque([n1])
    nearest = n1
    while q:
        common = q.popleft()
        if common in n1_parents and common in n2_parents:
            nearest = common
        q += tree_children[common]
    print(nearest)