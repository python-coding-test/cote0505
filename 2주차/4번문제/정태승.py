import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    n, d, c = map(int, sys.stdin.readline().split())

    graph = {i:[] for i in range(n)}
    pq = []

    def dijkstra(start):
        costs = {}
        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            cur_cost, cur_v = heapq.heappop(pq)

            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for cost, next_v in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_v))

        return (len(costs), max(costs.values()))


    for i in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b-1].append((s, a-1)) # (cost, node) 
    
    infects, time = dijkstra(c-1) 
    
    print(infects, time)
