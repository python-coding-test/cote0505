import sys, heapq

V, E = map(int, sys.stdin.readline().split())

graph = {
    v : [] for v in range(1, V+1)
}

K = int(sys.stdin.readline())

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    graph[u].append((w, v))

pq = [(0, K)]
costs = {}

while pq:
    cur_cost, cur_v = heapq.heappop(pq)

    if cur_v not in costs:
        costs[cur_v] = cur_cost
        for cost, nxt_v in graph[cur_v]:
            nxt_cost = cur_cost + cost
            heapq.heappush(pq, (nxt_cost, nxt_v))

for i in range(1, V+1):
    if i in costs:
        print(costs[i])
    else:
        print('INF')

# 우선순위 큐