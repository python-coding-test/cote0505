import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
dic = {i: set() for i in range(1, n+1)}

for i in range(m):
    a = str(sys.stdin.readline().strip())
    graph.append(a.split())

for i in range(len(graph)):
    train = int(graph[i][1])
    if graph[i][0] == '1':
        dic[train].add(int(graph[i][2]))
    elif graph[i][0] == '2':
        dic[train].discard(int(graph[i][2]))
    elif graph[i][0] == '3':
        new_set = set()
        for v in dic[train]:
            new_set.add(v + 1)
        dic[train] = new_set
        dic[train].discard(21)
    elif graph[i][0] == '4':
        new_set = set()
        for v in dic[train]:
            new_set.add(v - 1)
        dic[train] = new_set
        dic[train].discard(0)

isSeated = set()
for i in range(1, n + 1):
    temp = tuple(sorted(dic[i]))
    isSeated.add(temp)

print(len(isSeated))
