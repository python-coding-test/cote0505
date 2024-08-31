from itertools import combinations

def solution(cards):
    answer = 0
    n = len(cards)
    graph = [[] for i in range(n)]
    visited = [0]*len(cards)
    com = list(map(list, combinations(cards, 2)))
    group_sizes = []
    max_score = 0
        
    def dfs(cards, visited, start):
        group_size = 0
        cur = start
    
        while not visited[cur]:
            visited[cur] = 1
            next_box = cards[cur] - 1  # 카드 번호 = 다음 상자의 인덱스
            cur = next_box
            group_size += 1
    
        return group_size

    # 모든 상자 탐색 - 그룹 크기 구함
    for i in range(n):
        if not visited[i]:
            group_size = dfs(cards, visited, i)
            group_sizes.append(group_size)
    
    # 최대 점수 계산
    if len(group_sizes) > 1:
        for group1, group2 in combinations(group_sizes, 2):
            max_score = max(max_score, group1 * group2)
    
    return max_score
