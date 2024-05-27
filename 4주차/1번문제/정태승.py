from collections import defaultdict
import itertools

def solution(friends, gifts):
    give_and_takes = defaultdict(int) # 서로 주고받은 선물 수 정보
    gives = defaultdict(int) # 준 선물 수
    takes = defaultdict(int) # 받은 선물 수
    next_presents = defaultdict(int) # 다음달에 받을 선물
    
    for g in gifts:
        gs = g.split()
        give_and_takes[(gs[0], gs[1])] += 1 # g and t가 1이라는 의미는 t가 선물을 g에게 받았다는 의미. 즉 숫자가 커질수록 g가 선물을 받아야함.
        
        gives[gs[0]] += 1
        takes[gs[1]] += 1
    
    
    for c in list(itertools.combinations(friends, 2)):
        f = c[0]
        fr = c[1]
        
             # 1. 선물을 주고 받은 기록이 있다면,
        if give_and_takes[(f, fr)] > give_and_takes[(fr, f)]: # f가 준게 더 많다면
            next_presents[f] += 1
        elif give_and_takes[(f, fr)] < give_and_takes[(fr, f)]: # fr이 준게 더많다면
            next_presents[fr] += 1
        else: # 2. 선물을 주고 받은 기록이 없거나, 선물을 주고 받은 수가 같으면,
            f_p = gives[f] - takes[f]
            fr_p = gives[fr] - takes[fr] 

            if f_p > fr_p :
                next_presents[f] += 1
            elif f_p < fr_p :
                next_presents[fr] += 1
            else:
                next_presents[f] += 0
                next_presents[fr] += 0
     
    return max(next_presents.values())