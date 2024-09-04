def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    elif n == 2:
        return max(sticker)

    dp = [0] * (n-1)
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])

    dp2 = [0] * n
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])

    return max(dp[-1], dp2[-1])