#못풀어서 블로그 참고했습니다!
def solution(alp, cop, problems):
    maxAlp, maxCop = 0, 0

    for problem in problems:
        maxAlp = max(maxAlp, problem[0])
        maxCop = max(maxCop, problem[1])

    dp = [[150] * (maxCop+1) for _ in range(maxAlp+1)]
    # print(dp)

    # 최대알고력과 코딩력은 같은 문제에 있다는 보장X
    alp = min(alp, maxAlp)  # 둘중 하나라도 목표값을 넘어가면 안된다.
    cop = min(cop, maxCop)

    # dp[i][j] : 알고력 i, 코딩력 j을 도달 할 수 있는 최단시간
    dp[alp][cop] = 0

    for i in range(alp, maxAlp+1):
        for j in range(cop, maxCop+1):
            if i < maxAlp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < maxCop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            # problems 필요알고력, 필요코딩력, 증가알고력(보상), 증가코딩력(보상), 시간
            # i: 현재알고력, j:현재코딩력
            for problem in problems:
                if i >= problem[0] and j >= problem[1]:
                    # 문제를 해결한 후의 새로운 알고력과 코딩력 계산
                    nAlp = min(i+problem[2], maxAlp)  # 둘중 하나라도 목표값을 넘어가면 안된다.
                    nCop = min(j+problem[3], maxCop)
                    dp[nAlp][nCop] = min(dp[nAlp][nCop], dp[i][j] + problem[4])

    return dp[maxAlp][maxCop]

solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]])
solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])
