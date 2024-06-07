from collections import deque

def solution(n, m, x, y, r, c, k):
    short_path = abs(x-r) + abs(y-c)
    if short_path > k or (k-short_path) % 2:
        return 'impossible'

    dp = ['d','l','r','u']
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]

    q = deque([(x,y)])
    path = ''
    cnt = 0
    while q:
        x,y = q.popleft()

        if (x,y) == (r,c) and cnt == k:
            return path

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            np = dp[i]

            if 1<= nx <= n and 1<= ny <= m:
                if abs(nx-r) + abs(ny-c) + cnt+1 <= k:
                    path += np
                    q.append((nx,ny))
                    cnt += 1
                    break
    return 'impossible'


