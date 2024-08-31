def solution(cards):
    answer = 0
    curCards = set(cards)
    target = cards[0]
    cardGroup = []
    while curCards:
        group = 0
        while target in curCards:
            group += 1
            curCards.remove(target)
            target = cards[target-1]
        cardGroup.append(group)
        if len(curCards) > 0:
            target = list(curCards)[0]

    cardGroup.sort(reverse=True)
    answer = cardGroup[0]*cardGroup[1] if len(cardGroup)>1 else 0
    return answer