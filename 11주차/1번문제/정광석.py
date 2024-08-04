'''
합승 택시 요금

택시비 아끼기

택시 합승을 적절히 하면 택시 요금을 얼마나 아낄 수 있을지



'''

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]


import heapq



def solution(n, s, a, b, fares):
    answer = float('inf')

    graph = [[]*(n+1) for i in range(n+1)]

    for f in fares:
        start, end, fee= f
        # 양방향 이동 가능
        graph[start].append((end, fee))
        graph[end].append((start, fee)) 


    
  
    def dijkstra(start):
        queue = []
        distances = [float('inf')] * (n+1)
        distances[start] = 0
        heapq.heappush(queue, (distances[start],start))


       

        while queue:
            current_distance, current_dest = heapq.heappop(queue)

            if distances[current_dest] <  current_distance:
                continue
            for new_dest, new_distance in graph[current_dest]:
                distance = current_distance + new_distance
                if distance < distances[new_dest]:
                    distances[new_dest] = distance

                    heapq.heappush(queue, (distance, new_dest))

        return distances

    taxi_fee = [dijkstra(i) for i in range(n+1)]
    #print(taxi_fee)
    for i in range(n+1):
        answer = min(taxi_fee[s][i] + taxi_fee[i][a] + taxi_fee[i][b], answer)


    return answer


print(solution(n,s,a,b,fares))
