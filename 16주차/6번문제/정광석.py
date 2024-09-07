
sticker = [14, 6, 5, 11, 3, 9, 2, 10]

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    n = len(sticker)

    #1부터 시작
    dp1 = [0] * n
    select1 = [0] * n
    dp1[0] = sticker[0]
    select1[0] = 1
    dp1[1] = max(sticker[0], sticker[1])
    select1[1] = sticker[1] > sticker[0]


    for i in range(2, n - 1):
        if dp1[i-1] > dp1[i-2] + sticker[i]:
            dp1[i] = dp1[i-1]

        else:
            dp1[i] = dp1[i-2] + sticker[i]
            select1[i] = 1
            select1[i-1] = 0

    #print(dp1)
    #print(select1)

    #2부터 시작
    dp2 = [0] * n
    select2 = [0] * n
    dp2[1] = sticker[1]
    select2[1] = 1
    for i in range(2, n):
        if dp2[i-1] > dp2[i-2] + sticker[i]:
            dp2[i] = dp2[i-1]

        else:
            dp2[i] = dp2[i-2] + sticker[i]
            select2[i] = 1
            select2[i-1] = 0
    
    #print(select2)
    

    return max(dp1[n - 2], dp2[n - 1])
    

print(solution(sticker)) 
