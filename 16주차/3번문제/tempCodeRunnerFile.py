from collections import deque

N,M = map(int, input().split())

city = [input() for _ in range(N)]
road = deque()
visited = [0] * N
for i,v in enumerate(city):
    for i2,v2 in enumerate(v):
        if v2 == 'Y':
            visited[i] = 1
            if (i2,i) not in road and not visited[i2]:
                road.append((i,i2))
                visited[i2] = 1
# print(road)/
def main():
    global M
    if len(road) < M or sum(visited) != len(visited):
        print(-1)
        return

    visitCheck = [0] * N
    res = [0] * N
    while M:
        a,b = road.popleft()
        visitCheck[a] = 1
        visitCheck[b] = 1
        res[a] += 1
        res[b] += 1
        M -= 1
    # print(visited)
    # print(visitCheck)
    if(sum(visited)==sum(visitCheck)):
        print(*res)
    else:
        print(-1)

main()