from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0] # 정점, 도넛, 막대, 8자
    # edges는 index는 0부터 시작이지만 안의 값은 노드 번호
    node = set()  # 노드 갯수
    graph = {} # 나가는 간선
    graphin = defaultdict(int) # 들어오는 간선 기록
    
    for i in edges:
        a, b = i[0], i[1]
        node.add(a)
        node.add(b)
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
    
        graphin[b] = True
    
        
    for i in node: # 정점 구하기
        if i not in graphin:
            if len(graph[i]) >= 2:
                answer[0] = i
                break
    
    def dfs(start):
        q = [start]
        vis = {}
        while q:
            cur = q.pop()
                
            if not graph[cur]:  # 막대인 경우
                answer[2] += 1
                return
            
            elif len(graph[cur]) >= 2:
                answer[3] += 1
                return
            
            for i in graph[cur]:
                if (cur, i) not in vis:
                    q.append(i)
                    vis[(cur, i)] = 1
        answer[1] += 1
        return
    
    for i in graph[answer[0]]:
        dfs(i)
            
    return answer