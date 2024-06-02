from collections import defaultdict
from collections import deque
def solution(edges):
    answer = [0,0,0,0]  #생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수
    edge = set()
    adj = defaultdict(list) #갈 수 있는 노드
    goin = defaultdict(int) #진입하는 화살표
    goout = defaultdict(int) #밖으로 나가는 화살표
    for e in edges:
        adj[e[0]].append(e[1])
        edge.add(e[0])
        edge.add(e[1])
        goin[e[1]] +=1
        goout[e[0]] +=1
    #start찾기
    for i in edge:
        if goin[i] == 0 and len(adj[i]) >= 2:
            answer[0] = i
    def dfs(start):
        q = deque([start])
        vis = {}
        while q:
            a = q.popleft()
            #막대모양 그래프인 경우
            if len(adj[a]) == 0:
                answer[2] +=1
                return
            #8자 그래프의 경우
            elif len(adj[a]) >=2:
                answer[3]+=1
                return
            for i in adj[a]: #q에 있는 노드
                if len(adj[i])>=2:
                    answer[3]+=1
                    return
                if (a, i) in vis: #방문된 edge이면 pass
                    continue
                q.append(i) 
                vis[(a,i)] = True
        answer[1]+=1
        return
                     
    for i in adj[answer[0]]:
        dfs(i)
    return answer
print(solution(	[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], 
                 [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], 
                 [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))