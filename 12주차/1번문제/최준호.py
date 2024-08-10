def solution(N, stages):
    answer = []

    people = len(stages)

    challenge = [0] * (N+1)
    for i in stages:
        challenge[i-1] += 1

    fail = []
    for i in range(N):
        if not people:
            fail.append([0,i+1])
            continue

        stay = challenge[i]
        fail.append([stay / people, i+1])
        people -= stay

    fail.sort(key = lambda x :(-x[0], x[0]))
    res = []
    for i in fail:
        res.append(i[1])

    return res