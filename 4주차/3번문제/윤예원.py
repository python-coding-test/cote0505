
#정확성: 50.0
import random
from itertools import combinations, product
def sum_of_combinations(arrays):
    all_combinations = product(*arrays)
    sums = [sum(combination) for combination in all_combinations]
    
    return sums
def solution(dice):
    n = len(dice) //2
    best_comb = None
    max_win_prob = 0
    a_comb = list(combinations(range(len(dice)), n))
    for a in a_comb:
        b = set(range(len(dice))) - set(a)
        a_arr = [dice[i] for i in a]
        b_arr = [dice[i] for i in b]
        
        a_score = sum_of_combinations(a_arr)
        b_score = sum_of_combinations(b_arr)
        win = same = lose = 0
        for i in a_score:
            for j in b_score:
        
                if i > j:
                    win += 1
                elif i == j:
                    same += 1
                else:
                    lose += 1
        win_prob = win/(win+same+lose)
        if win_prob > max_win_prob:
            max_win_prob = win_prob
            best_comb = a
    best_comb = [x+1 for x in best_comb]
    return sorted(best_comb)