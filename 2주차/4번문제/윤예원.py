import heapq, sys
input = sys.stdin.readline
INF = 1e9
t = int(input())
def dijkstra(start):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))         
    distance[start] = 0
    while q:
          dist, now = heapq.heappop(q)
          if distance[now] < dist:
               continue
          for i in graph[now]:
               cost = dist+i[1]
               if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    count, max_distance = 0, 0
    for d in distance:
         if d!= INF:
              count+=1
              max_distance = max(max_distance, d)
    print(count-1, max_distance)

for _ in range(t):
    n,d,c = map(int, input().split())
    graph = [[] for i in range(n+1)]
    
    for _ in range(d):
         a,b,s = map(int, input().split())
         graph[b].append((a,s))
    dijkstra(c)
    
    

                    
