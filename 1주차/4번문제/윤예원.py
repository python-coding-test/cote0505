#블로그 참고
n, k =map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
lst = [[0,0]]
for i in range(n):
    lst.append(list(map(int, input().split())))
for i in range(1, n+1):
    for j in range(1,k+1):
        weight = lst[i][0]
        value = lst[i][1]
        if j < weight: #가방에 넣을 수 없으면
            dp[i][j] = dp[i-1][j]
        else: #가방에 넣을 수 있으면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[n][k])

#https://velog.io/@dmsgur7112/Knapsack%EB%B0%B0%EB%82%AD-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98