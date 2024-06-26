#gpt풀이
MOD = 1000000009
dp = [[0 for _ in range(4)] for _ in range(100001)] 

dp[1][1] =1
dp[2][2] =1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for n in range(4, 100001):
    dp[n][1]= (dp[n-1][2]+dp[n-1][3]) % MOD
    dp[n][2] = (dp[n-2][1]+dp[n-2][3]) % MOD
    dp[n][3] = (dp[n-3][1]+dp[n-3][2]) %MOD

t=int(input())
for _ in range(t):
    n = int(input())
    print(sum(dp[n])%MOD)