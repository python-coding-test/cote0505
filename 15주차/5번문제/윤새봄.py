from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for p in permutations(dungeons, len(dungeons)):
        power = k
        number = 0
        for lower_bound, consume in p:
            if (power >= lower_bound):
                power-=consume
                number += 1
                
        answer = max(answer, number)
    
    return answer