from collections import deque, defaultdict

def solution(edges, target):
    graph = defaultdict(list)
    for u, v in edges:
            print(u,v)
            graph[u].append(v)
            graph[v].append(u)

    queue = deque([(1, [1], [1])])
    min_dropped = float('inf')
    min_sequence = []

    while queue:
        node, path, dropped = queue.popleft()
        if node == len(edges) + 1:
            if sum(target) == sum(dropped):
                if len(dropped) < min_dropped or (len(dropped) == min_dropped and dropped < min_sequence):
                    min_dropped = len(dropped)
                    min_sequence = dropped[:]
        else:
            for child in sorted(graph[node], key=lambda x: x):
                if child == path[-1]:
                    new_path = path + [child]
                    new_dropped = dropped + [node]
                    queue.append((child, new_path, new_dropped))
                elif child not in path:
                    new_path = path + [child]
                    new_dropped = dropped + [node]
                    queue.append((child, new_path, new_dropped))

    if not min_sequence:
        return [-1]
    return min_sequence

solution([[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]], [0, 0, 0, 3, 0, 0, 5, 1, 2, 3])