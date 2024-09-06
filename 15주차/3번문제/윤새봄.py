def solution(cards):
    answer = []
    visited = [False]*(len(cards)+1)
            
    for card in cards:
        if (visited[card-1]):
            continue
        temp = []
        while card not in temp:
            temp.append(card)
            visited[card-1]=True
            card = cards[card-1]
        answer.append(len(temp))
        
    if (answer[0]==len(cards)):
        return 0
    
    answer.sort(reverse=True)
    
    return answer[0]*answer[1]