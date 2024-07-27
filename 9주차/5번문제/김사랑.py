def solution(info, edges):
    answer = []  # 양의 수를 저장할 리스트
    visited = [0] * len(info)  # 각 노드 방문 여부를 저장하는 리스트

    def dfs(sheep, wolf):
        # 양의 수가 늑대의 수보다 많을 때만 결과에 저장
        if sheep > wolf:
            answer.append(sheep)
        else:
            return  # 양의 수가 늑대의 수보다 적거나 같으면 종료
        
        # 각 간선을 순회
        for a, b in edges:
            # 현재 노드가 방문되었고, 다음 노드가 방문되지 않았을 때
            if visited[a] and not visited[b]:
                visited[b] = 1  # 다음 노드를 방문 표시
                
                # 다음 노드가 양일 때, 양의 수 증가
                if info[b] == 0:
                    dfs(sheep + 1, wolf)
                    
                else:  # 다음 노드가 늑대일 때, 늑대의 수 증가
                    dfs(sheep, wolf + 1)
                visited[b] = 0  # 다음 노드 방문 상태를 0으로 변경

    visited[0] = 1  # 시작 노드 방문 표시 (루트 노드)
    dfs(1, 0)  # 초기 양의 수는 1, 늑대의 수는 0으로 시작
    
    return max(answer)  # 최대 양의 수 반환
