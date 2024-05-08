import sys

N = int(sys.stdin.readline())

bd = { i : list(map(int, sys.stdin.readline().split())) for i in range(N) }
dp = {}

def go(level, nth):
    if level == N:
        return 0
    
    if (level, nth) in dp:
        return dp[(level, nth)]
    
    dp[(level, nth)] = max(go(level+1, nth) + bd[level][nth], go(level+1, nth+1) + bd[level][nth])
    
    return dp[(level, nth)]
    #왼쪽 대각선 or 오른쪽 대각선

print(go(0, 0))