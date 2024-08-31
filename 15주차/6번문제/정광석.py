'''
n개의 송전탑 전선 하나 트리

하나 끊어서 전력망 네트웤 2개 분할

갯수 최대한 비슷하게 맞추기

전선 중 하나를 끊어서 송전탑 갯수가 가능한 비슷하도록 두 전력망으로 나누었을 때 송전탑 개수 차이 return

'''


n, wires = 9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]


def solution(n, wires):
    def find_parent(a):
        if parent[a] != a:
            parent[a] = find_parent(parent[a])
        return parent[a]
    
    def union(a, b):
        root_a = find_parent(a)
        root_b = find_parent(b)
        if root_a != root_b:
            parent[root_b] = root_a
    
    min_diff = n
    
    for i in range(len(wires)):
        
        parent = [i for i in range(n + 1)]
        
        for j in range(len(wires)):
            if i == j:
                continue
            w1, w2 = wires[j]
            union(w1, w2)
        
        
        count = [0 for _ in range(n+1)]
        for k in range(1, n + 1):
            count[find_parent(k)] += 1
        
        
        group_sizes = [x for x in count if x > 0]
        
        if len(group_sizes) == 2:
            diff = abs(group_sizes[0] - group_sizes[1])
            min_diff = min(min_diff, diff)
    
    return min_diff



print(solution(n, wires))  