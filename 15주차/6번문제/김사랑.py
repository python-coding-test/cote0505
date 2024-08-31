def solution(n, wires):
    # answer = -1
    graph = [[] for _ in range(n+1)]
    # visited = [[0] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(node):
        cnt = 1
        visited[node] = 1
        for child in graph[node]:
            if visited[child] == 0:
                cnt += dfs(child) 
        return cnt
    
    min_v = float('inf')
    
    for a, b in wires:
        visited = [0] * (n+1)
        graph[a].remove(b)
        graph[b].remove(a)
        
        cnta = dfs(a)
        cntb = n - cnta
        min_v = min(min_v, abs(cnta-cntb))
        
        graph[a].append(b)
        graph[b].append(a)
        
    return min_v
