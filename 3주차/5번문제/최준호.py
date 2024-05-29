import heapq, sys
from collections import defaultdict

V, E = map(int, input().split())
K = int(input())

edge = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edge[u].append((v, w))

res = [float('inf')] * (V + 1)
res[K] = 0
q = [(0, K)]
while q:
    d, v = heapq.heappop(q)

    for nv, w in edge[v]:
        nd = d + w
        if nd < res[nv]:
            res[nv] = nd
            heapq.heappush(q, (nd, nv))

for i in range(1, V + 1):
    print(res[i] if res[i] != float('inf') else 'INF')
