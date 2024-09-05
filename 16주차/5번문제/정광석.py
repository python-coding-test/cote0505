'''
n개 마을 이루어진 나라, 1~N 번호 하나씩 부여
양방향도로 연결됨

도로 지날 때 걸리는 시간 다 다름

1에서 각 마을로 배달
K시간  이하로 배달 가능한 곳 에서만 주문 받기




'''

N, road, K = 6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4


def solution(N, road, K):
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    visited = [False] * (N+1)  

  
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))


    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                idx = i
        return idx

    # 다익스트라
    def dijkstra(start):
        distance[start] = 0 
        
      
        for _ in range(N):
            now = get_smallest_node()  
            visited[now] = True 

            for next_node, time in graph[now]:
                cost = distance[now] + time
                
                if cost < distance[next_node]:
                    distance[next_node] = cost

    dijkstra(1)

    # K 이하로 배달 가능한 마을의 개수 계산
    answer = sum(1 for d in distance if d <= K)
    
    return answer


print(solution(N, road, K)) 

