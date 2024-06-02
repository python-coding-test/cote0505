def solution(coin, cards):
    n = len(cards)
    hand = cards[:len(cards)/3]
    stage = 0
    if len(hand) == 0:
        return
    cur_ind = len(cards)/3-1
    #2장을 받는 경우
    def go(hand, cur_ind):

    def go1(hand,cur_ind):
    
    



    for i in range(len(hand)):
        for j in range(i+1, len(hand)):  # 중복을 피하기 위해 j는 i+1부터 시작합니다.
            if hand[i] + hand[j] >= n+1:
                if coin >0:
                
                    
                    #추가로 받는 경우
                            go(hand, cur_ind)
                    #2장을 받지 않는 경우
                            go1(hand, cur_ind)


    answer = 0
    return answer





