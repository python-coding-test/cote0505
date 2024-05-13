import sys
sys.setrecursionlimit(10**5)

N, K = map(int, sys.stdin.readline().split())
bd = list(map(int, sys.stdin.readline().split()))
dp = {}

def go(curr):
    if curr in dp: # 0이라는 값이 return 됐다면, 해당 curr에서는 절대 N까지 도달불가.
        return 0

    if curr == N-1 :
        print('YES')
        exit()

    dp[curr] = 0 
    for j in range(curr+1, N): # i에서 시작해 j로 가능한 이동.
        strength = (j-curr)*(1+abs(bd[curr]-bd[j]))
        if strength > K:
            continue

        dp[curr] = go(j)
    
    return dp[curr]

go(0)

print('NO')