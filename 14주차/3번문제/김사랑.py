from collections import Counter

def solution(picks, minerals):
    answer = 0
    temp = []
    
    if len(minerals) > 5 * sum(picks):
        minerals = minerals[:5 * sum(picks)]
    
    for i in range(0, len(minerals), 5):
        cnt = Counter(minerals[i:i+5])
        temp.append((cnt['diamond'], cnt['iron'], cnt['stone']))
        
    temp.sort(reverse=True)
    
    for n_dia, n_iron, n_stone in temp:
        if picks[0] > 0:
            answer += n_dia * 1 + n_iron * 1 + n_stone * 1
            picks[0] -= 1
        elif picks[1] > 0:
            answer += n_dia * 5 + n_iron * 1 + n_stone * 1
            picks[1] -= 1
        else:
            answer += n_dia * 25 + n_iron * 5 + n_stone * 1
            picks[2] -= 1

    return answer
