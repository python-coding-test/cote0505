import sys
sys.setrecursionlimit(10**5)

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break
    
    ns = []
    dp = {}
    ans = -10001
    for i in range(0, N):
        n = int(sys.stdin.readline())
        ns.append(n)

    def go(level):
        if level == N-1 :
            return ns[level]
        
        if level in dp:
            return dp[level]

        dp[level] = max(ns[level], go(level+1) + ns[level]) # 선택 안함 or 선택함

        return dp[level]


    for i in range(N):
        ans = max(ans, go(i))

    print(ans)