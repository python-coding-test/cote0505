# 블로그 참고했습니다
# https://velog.io/@statco19/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B3%BC-%EB%8A%91%EB%8C%80

def dfs(cur, w, s, childrens, info, graph):
    animal = info[cur]
    if animal == 0:
        s += 1
    else:
        w += 1

    if w >= s:
        return s

    max_sheep = s

    for i in range(len(childrens)):
        children = childrens[:]
        child = children.pop(i)
        children += graph[child]
        max_sheep = max(max_sheep, dfs(child, w, s, children, info, graph))

    return max_sheep

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])

    return dfs(0, 0, 0, graph[0], info, graph)
