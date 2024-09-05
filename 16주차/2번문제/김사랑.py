import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    tree = {}
    for j in range(n-1):
        parent, child = map(int, sys.stdin.readline().split())
        tree[child] = parent
    a, b = map(int, sys.stdin.readline().split())
    a_parents = set()  # O(1)
    while a in tree:
        a_parents.add(a)
        a = tree[a]
    a_parents.add(a)  # 루트 추가
    
    while b not in a_parents:
        b = tree[b]
    print(b)
