# 3:20~4:04
def solution(info, edges):
    answer = 0
    N = len(info) # node의 개수.
    sheep_plus = [1, 0]
    wolf_plus = [0, 1]
    
    # 인접리스트 생성
    adj = {i:[] for i in range(N)}
    for e in edges:
        adj[e[0]].append(e[1])
    
    # 현재 상태에서 갈 수 있는 노드 알려주기.
    def find_can_go_nodes(visits):
        can_go_nodes = []
        
        for v in visits:
            for e in adj[v]:
                if e not in visits:
                    can_go_nodes.append(e)
                    
        return can_go_nodes
    
    def go(sheep, wolf, visits):        

        nonlocal answer
        answer = max(answer, sheep)
            
        if len(visits) == N:
            return
        
        can_go_nodes = find_can_go_nodes(visits)
        
        for node in can_go_nodes:
            
            nxt_sheep = sheep + sheep_plus[info[node]]
            nxt_wolf = wolf + wolf_plus[info[node]]
            
            if nxt_wolf >= nxt_sheep:
                continue
            
            visits.append(node)
            go(nxt_sheep, nxt_wolf, visits)
            visits.pop()
        
        
        return
            
    go(1, 0, [0])
        
    
    return answer




# 양 모으기. -> 각 노드에 있던 양과 늑대가 따라옴.
# 늑대수>=양수 -> 모든 양 잡아먹힘.
# 최대한 많은 양 수 모으기.
# 0 -> 양 1 -> 늑대