N,K = map(int, input().split())
bridge = list(map(int, input().split()))
dp = [0] * (N+1)
for i in range(1,N+1):
    if dp[i] < 0:
        continue

    for j in range(i+1,N+1):
        need = (j-i)*(1+abs(bridge[i-1]-bridge[j-1]))
        if need > K:
            if dp[j] > 0:
                continue
            dp[j] = -1
        else:
            if dp[j] <= 0:
                dp[j] =  need+dp[i]
            else:
                dp[j] = min(dp[j], need+dp[i])
print("YES" if dp[-1] >0 else "NO" )