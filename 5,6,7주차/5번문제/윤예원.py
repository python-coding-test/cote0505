from collections import deque
def solution(n,m,x,y,r,c,k):
    dist = abs(x-r)+abs(y-c) #목표물까지 남은 거리
    if dist > k or (k-dist)%2:
        return "impossible"
    dx = [1,0,0,-1]#dlru
    dy = [0,-1,1,0]
    queue =deque([(x,y)])  # (x, y)
    path = ""
    cnt = 0
    while queue:
        x,y = queue.popleft()
        if x == r and y == c and cnt == k:
            return path
        if cnt > k:
            break
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 1<=nx<=n and 1<=ny<=m and cnt < k:
                if abs(nx-r) + abs(ny-c) + cnt+1 <= k:
                    queue.append((nx,ny))
                    path += "dlru"[i]
                    cnt+=1
                    break
    print(path)

    return "impossible"

print(solution(3,4,2,3,3,1,5))