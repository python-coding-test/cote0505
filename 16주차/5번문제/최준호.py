def solution(N, road, K):
    graph = [[500000]*(N+1) for _ in range(N+1)]

    for i in range(1,N+1):
        graph[i][i] = 0

    for i in road:
        a,b,c = i
        if graph[a][b] > c:
            graph[a][b] = c

        if graph[b][a] > c:
            graph[b][a] = c

    for k in range(1,N+1):
        for x in range(1,N+1):
            for y in range(1,N+1):
                graph[x][y] = min(graph[x][y] , graph[x][k]+graph[k][y])

    res = 0
    for time in graph:
        if time[1] <=K:
            res+=1
    return res