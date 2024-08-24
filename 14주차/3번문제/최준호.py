from collections import deque

def solution(picks, minerals):
    answer = 0

    demage = {
        "diamond" : [1,5,25],
        "iron" : [1, 1, 5],
        "stone" : [1, 1, 1]
    }

    q = deque(minerals)
    demands = []
    picksLength = sum(picks)
    while q:
        demand = [0,0,0]
        for _ in range(5):
            if not q:
                break
            mineral = q.popleft()
            demand[0] += demage[mineral][2]
            demand[1] += demage[mineral][1]
            demand[2] += demage[mineral][0]
        demands.append(demand)
        if len(demands) >= picksLength:
            break

    demands.sort(reverse=True)

    for demand in demands:
        if picks[0] > 0:
            answer += demand[2]
            picks[0] -= 1
        elif picks[1] > 0:
            answer += demand[1]
            picks[1] -= 1
        elif picks[2] > 0:
            answer += demand[0]
            picks[2] -= 1
        else:
            break

    return answer