def solution(friends, gifts):
    peopleIdx = {}
    for i,v in enumerate(friends):
        peopleIdx[v] = i

    info = [[0]*len(friends) for _ in range(len(friends))]
    for i in gifts:
        giver, receiver = i.split()
        gIdx = peopleIdx[giver]
        rIdx = peopleIdx[receiver]

        info[gIdx][rIdx] += 1
        info[rIdx][gIdx] -= 1

    giftFactor = {}
    for i in range(len(friends)):
        giftFactor[i] = sum(info[i])

    nextGift = [0]*len(friends)
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            if info[i][j] > 0:
                nextGift[i] += 1

            elif info[i][j] < 0:
                nextGift[j] += 1

            else:
                if giftFactor[i] == giftFactor[j]:
                    continue

                idx = i if giftFactor[i] > giftFactor[j] else j
                nextGift[idx]+= 1

    return max(nextGift)