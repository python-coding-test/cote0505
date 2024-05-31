from itertools import combinations
from collections import deque

def solution(coin, cards):
    
    # 최초 세팅
    N = len(cards)
    hands = {cards[i]: True for i in range(N//3)}
    card_bundle = deque([cards[i] for i in range(N//3, N)])
    
    def isNplus1(handss): # 현재 손패에서 N+1 조합이 가능하냐?
        for k, v in handss.items():
            if ((N+1)-k) in handss: # N+1-k 값이 handss에 존재하면 가능.
                return True
        return False
        
    
    def go(handss, card_b, coins): # 손패 / 카드뭉치 / 동전
        if not card_b: # 카드 뭉치가 비면 종료.
            return 0
        
#         if len(handss) <= 1 : # 손패가 1장 이하이거나 카드 뭉치가 비어있다면 종료.
#             return 0
        
        # if not isNplus1(handss): # 현재 손패에서 낼카드가 없다면 종료시키기.
        #     return 0
        
        rounds = 1
        
        # 0. 카드 2장 드로우
        nxt_1 = card_b.popleft()
        nxt_2 = card_b.popleft()
        
        # 1. 2개 소모한 경우
        if coins >= 2:
            handss[nxt_1] = True
            handss[nxt_2] = True
            coins-=2
            handss_cp = handss.copy()
            for k, v in handss.items():
                if (N+1)-k in handss:
                    del handss_cp[(N+1)-k]
                    del handss_cp[k]  
                    rounds = max(rounds, go(handss_cp, card_b, coins)+1)
                    handss_cp[(N+1)-k] = True
                    handss_cp[k] = True

            coins+=2
            del handss[nxt_1]
            del handss[nxt_2]
        
        # 2. 1개 소모한 경우 
        if coins >= 1:
            
            # 2-1. nxt_1
            handss[nxt_1] = True
            coins-=1
            handss_cp = handss.copy()
            for k, v in handss.items():
                if (N+1)-k in handss:
                    del handss_cp[(N+1)-k]
                    del handss_cp[k]  
                    rounds = max(rounds, go(handss_cp, card_b, coins)+1)
                    handss_cp[(N+1)-k] = True
                    handss_cp[k] = True
            
            coins+=1
            del handss[nxt_1]
    
            # 2-2. nxt_2
            handss[nxt_2] = True
            coins-=1
            handss_cp = handss.copy()

            for k, v in handss.items():
                if (N+1)-k in handss:
                    del handss_cp[(N+1)-k]
                    del handss_cp[k]  
                    rounds = max(rounds, go(handss_cp, card_b, coins)+1)
                    handss_cp[(N+1)-k] = True
                    handss_cp[k] = True
            
            coins+=1
            del handss[nxt_2]
        
        # 3. 아예 코인 소모 안한 경우.
        
        handss_cp = handss.copy()
        for k, v in handss.items():
            if (N+1)-k in handss:
                del handss_cp[(N+1)-k]
                del handss_cp[k]  
                rounds = max(rounds, go(handss_cp, card_b, coins)+1)
                handss_cp[(N+1)-k] = True
                handss_cp[k] = True
                
        return rounds
        
    answer = go(hands, card_bundle, coin)
    
    return answer

# 20점 코드입니다.