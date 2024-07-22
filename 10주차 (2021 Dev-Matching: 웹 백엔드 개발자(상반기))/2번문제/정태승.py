def solution(lottos, win_nums):
    answer = []
    hit = 0
    zero_check = 0
    
    for i in range(6):
        if lottos[i] in win_nums :
            hit+=1
        elif lottos[i] == 0:
            zero_check+=1
    
    max_rank = abs((hit+zero_check)-7) if 1 <= abs((hit+zero_check)-7) <= 5 else 6
    min_rank = abs((hit)-7) if 1 <= abs((hit)-7) <= 5 else 6
    
    answer.append(max_rank)
    answer.append(min_rank)
    
    return answer