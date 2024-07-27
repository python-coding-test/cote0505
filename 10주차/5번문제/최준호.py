# 정확성만 통과한 코드입니다.

from collections import defaultdict
from bisect import bisect_left

language = defaultdict(set)
position = defaultdict(set)
career = defaultdict(set)
soul_food = defaultdict(set)
scores = defaultdict(set)

def solution(info, query):
    answer = []
    for i,v in enumerate(info):
        l,p,c,s,score = v.split()
        language[l].add(i)
        position[p].add(i)
        career[c].add(i)
        soul_food[s].add(i)
        scores[int(score)].add(i)

        language['-'].add(i)
        position['-'].add(i)
        career['-'].add(i)
        soul_food['-'].add(i)

    scores_keys = sorted(list(scores.items()))

    for q in query:
        conditions = q.split(" and ")
        conditions += conditions.pop().split()

        candidates = language[conditions[0]] & position[conditions[1]] & career[conditions[2]] & soul_food[conditions[3]]

        idx = bisect_left(scores_keys, (int(conditions[4]),set()))
        temp = set()
        for i in scores_keys[idx:]:
            a,b= i
            temp = temp | b

        answer.append(len(candidates & temp))

    return answer