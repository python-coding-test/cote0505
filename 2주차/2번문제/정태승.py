import sys
sys.setrecursionlimit(10**5)

N, M = map(int, sys.stdin.readline().split())
bd = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


dp = {}
def go(sx, sy):
    if sx < 0 or sy < 0 or sx >= N or sy >= M:
        return 0

    if sx==N-1 and sy==M-1:
        return bd[sx][sy]
    
    if (sx, sy) in dp:
        return dp[(sx, sy)]

    dp[(sx, sy)] = bd[sx][sy] + max(go(sx, sy+1), go(sx+1, sy))
        
    return dp[(sx, sy)]

print(go(0, 0))