from itertools import combinations

def solution(dice):
    answer = []
    
    
    # 1. 주사위 일대일 기록하기.
    one_to_one_dice = {} # (i, j)=1,0,-1 : i가 j를 상대로 승,무,패.
    dices_indexs = [i for i in range(len(dice))]
    
    def one_to_one_compare(d1, d2, i, j):
        d1_w = 0
        d2_w = 0
        
        for d1i in range(6):
            for d2i in range(6):
                if d1[d1i] > d2[d2i]:
                    d1_w+=1
                elif d1[d1i] < d2[d2i]:
                    d2_w+=1
            
        if d1_w > d2_w:
            one_to_one_dice[(i, j)] = 1
            one_to_one_dice[(j, i)] = -1
            return
        elif d1_w == d2_w:
            one_to_one_dice[(i, j)] = 0
            one_to_one_dice[(j, i)] = 0
            return 0
        else:
            one_to_one_dice[(i, j)] = -1
            one_to_one_dice[(j, i)] = 1
            return -1
            
    
    for i in range(len(dice)):
        for j in range(i+1, len(dice)):
            one_to_one_compare(dice[i], dice[j], i, j)

    
    # 2. nCn//2로 분배
    mx_score = -1
    for ours in list(combinations(dices_indexs, len(dice)//2)):
        
        
        # 3. 주사위 1:1 기록을 바탕으로 승/패 구해서 확률 구하기
        others = list(set(dices_indexs) - set(ours))
        win_score = 0        
        
        for u in ours:
            for o in others:
                if one_to_one_dice[(u, o)] == 1:
                    win_score+=1
                
                    
        if mx_score < win_score:
            mx_score = win_score
            answer = ours  

    return list(map(lambda n: n+1, answer))

# 71.9/100 풀이입니다 