from collections import deque
from collections import defaultdict

def solution(edges):
    answer = [0,0,0,0] # 정점번호, 도넛수, 막대수, 8자수
    
    adj = {} # 인접그래프
    es = set() # 모든 정점
    ess = defaultdict(int) # 지목당하는거 개수세기용. 기본 초기값 -1
    
    for e in edges:
        if e[0] not in adj :
            adj[e[0]] = []
        if e[1] not in adj :
            adj[e[1]] = []
        
        es.add(e[0])
        es.add(e[1])
        ess[e[1]]=True
        
        adj[e[0]].append(e[1])

    # 자신이 하나도 지목되지 않고, 연결된 정점이 2개 이상인 경우, 새로 생성된 정점 (항상 도넛,막대,8자 수 는 2개 이상이므로)
    for e in es:
        if e not in ess and len(adj[e]) >= 2:
            answer[0] = e
        
    def go(st):
        vis = {}
        q = [st] # dfs 
        
        while q:
            cur = q.pop()
            
            if not adj[cur]: # 해당 정점에서 아무곳도 갈 수 없다면 => 막대그래프.
                answer[2]+=1
                return 
            
            for nxt in adj[cur]:
                if len(adj[cur]) >= 2: # 어느 한점이 두 곳 이상 이동할 수 있는 경로가 있다면 => 8자
                    answer[3]+=1 
                    return
                
                if (cur, nxt) in vis:  # 방문한 edge인지 확인
                    continue
                
                q.append(nxt)
                vis[(cur, nxt)] = True
        answer[1]+=1    
        return
    
    # 2. 찾은 정점 번호로 순회하기.
    for st in adj[answer[0]]:
        go(st)
    
    
    return answer

# 1시간반 풀이 ㅠ

