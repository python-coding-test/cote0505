from collections import deque

n = int(input())
bridge = list(map(int, input().split()))
s = int(input())

q = deque([s-1])
visited = [0]*n
while q:
    idx = q.popleft()
    visited[idx] = 1

    dx = [bridge[idx], -bridge[idx]]
    for i in dx:
        nx = idx + i
        if 0<= nx <n and not visited[nx]:
            q.append(nx)
print(sum(visited))