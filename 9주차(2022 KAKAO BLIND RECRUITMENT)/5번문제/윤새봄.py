answer = 0

def dfs(sheep, wolf, info, edges, visited):
    global answer
    
    if (sheep > wolf):
        if (answer < sheep):
            answer = sheep
    else:
        return
    
    for parent, child in edges:
        if visited[parent] == 1 and visited[child] == 0:
            # 해당 노드 방문
            visited[child] = 1
            if (info[child]==0): # 해당 노드에 양이 있으면,
                dfs(sheep+1, wolf, info, edges, visited)
            else: # 해당 노드에 늑대가 있으면,
                dfs(sheep, wolf+1, info, edges, visited)
            
            visited[child] = 0
                
    

def solution(info, edges):
    global answer
    
    visited = [0]*len(info)
    
    # 루트 노드(0)에서 출발. 
    visited[0] = 1
    
    # DFS로 풀기.
    # 루트 노드에는 항상 양이 있음.
    dfs(1, 0, info, edges, visited)
    
    return answer
