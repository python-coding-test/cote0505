N, K = map(int, input().split())
dp = [0] * (K + 1)  # dp[i]는 배낭의 무게가 i일 때, 최대 가치합

for _ in range(N):
    W, V = map(int, input().split())
    # 무게 한계 K부터 시작하여 현재 물건의 무게 W까지 역순으로 탐색
    for i in range(K, W-1, -1):
        # 현재 물건을 추가했을 때와 추가하지 않았을 때의 가치 중 더 큰 값을 선택
        dp[i] = max(dp[i], dp[i-W] + V) # dp[i-W] : 현재 물건을 넣기 전까지의 최대 가치

print(dp[K])  # 최대 가치합 출력
#Gpt 참조