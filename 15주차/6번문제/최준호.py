from collections import deque, defaultdict

def dfs(tower,tree):
    visited = {}
    for i in tower:
        visited[i] = False

    diff = []
    for i in tower:
        if visited[i]:
            continue

        cnt = 0
        q = deque(list(tree[i]))
        if not q:
            cnt = 1

        while q:
            t = q.popleft()
            if visited[t]:
                continue

            cnt += 1
            visited[t] = True
            q += list(tree[t])

        diff.append(cnt)
    return abs(diff[0]-diff[1])

def solution(n, wires):
    tree = defaultdict(set)
    for i in wires:
        tree[i[0]].add(i[1])
        tree[i[1]].add(i[0])

    tower = tree.keys()

    min_diff = len(tower)
    for i in wires:
        tree[i[0]].remove(i[1])
        tree[i[1]].remove(i[0])

        min_diff = min(min_diff, dfs(tower,tree))

        tree[i[0]].add(i[1])
        tree[i[1]].add(i[0])

    return min_diff