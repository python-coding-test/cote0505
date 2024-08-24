from collections import deque
from bisect import bisect_right

def solution(scores):
    answer = 0

    target = scores[0]
    # q = deque(sorted(scores,reverse=True))
    scores.sort(key=lambda x: (-x[0], x[1]))
    q = deque(scores)
    peerScore = q[0][1]
    for _ in range(len(q)):
        i = q.popleft()
        if i[1] < peerScore:
            if i == target:
                return -1
            continue
        elif i[1] > peerScore:
            peerScore = i[1]
        q.append(sum(i))

    score = len(q) - bisect_right(sorted(q),sum(target)) + 1

    return score