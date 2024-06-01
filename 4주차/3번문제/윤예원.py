
#정확성: 50.0
import random
from itertools import combinations, product
def solution(dice):
    n = len(dice) //2
    best_comb = None
    max_win_prob = 0
    a_comb = list(combinations(range(len(dice)), n))
    for a_comb in combinations(range(len(dice)), n):
        win = same = lose = 0
        a_dice = [dice[i] for i in a_comb]
        b_dice = [dice[i] for i in range(len(dice)) if not i in a_comb]
        for a_outcome in product(*a_dice):
            a_score = sum(a_outcome)
            for b_outcome in product(*b_dice):
                b_score = sum(b_outcome)
                if a_score > b_score:
                    win += 1
                elif a_score == b_score:
                    same += 1
                else:
                    lose += 1
        win_prob = win/(win+same+lose)
        if win_prob > max_win_prob:
            max_win_prob = win_prob
            best_comb = a_comb
    best_comb = [x+1 for x in best_comb]
    return sorted(best_comb)