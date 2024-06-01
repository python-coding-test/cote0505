from collections import defaultdict, deque

def solution(edges):
    edge = defaultdict(list)
    target = defaultdict(list)
    for i in edges:
        s,e = i
        edge[s].append(e)
        if s == e:
            continue
        target[e].append(s)

    start = 0
    n = max(target)
    for i in range(1,n+1):
        if i not in target and len(edge[i]) >= 2:
            start = i
    res = [start,0,0,0]
    visited = [0] * (n+1)

    for i in edge[start]:
        n_len = 0
        w_len = 0

        q = deque([i])
        while q:
            node = q.popleft()

            if visited[node]:
                continue

            visited[node] = 1
            n_len += 1
            if not edge[node]:
                break

            q += edge[node]
            w_len += len(edge[node])

        if n_len == w_len:
            res[1] += 1
        elif n_len > w_len:
            res[2] += 1
        else:
            res[3] += 1
    return res