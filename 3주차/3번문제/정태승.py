import sys

N, M = map(int, sys.stdin.readline().split())

K = int(sys.stdin.readline())

blocked = {}
dp = {}
for i in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split()) # (a,b), (c,d)
    blocked[(c,d,a,b)] = True
    blocked[(a,b,c,d)] = True


def go(cx, cy, level):

    if cx == N and cy == M and level == N+M:
        return 1
    
    if level >= N+M or cx > N or cy > M :
        return 0
    
    if (cx, cy) in dp:
        return dp[(cx, cy)]

    dp[(cx, cy)] = 0
    for d in [(1,0), (0,1)]:
        nx = cx + d[0]
        ny = cy + d[1]

        if (cx, cy, nx, ny) in blocked:
            continue
        
        dp[(cx, cy)] += go(nx, ny, level+1)
    
    return dp[(cx, cy)]



print(go(0,0,0))