def solution(N, stages):
    answer = []
    temp = []
    for i in range(1, N+1):
        current_len = len(stages)
        failure_rate = 0  # 실패율
        failed = 0
        for j in range(len(stages)):
            if stages[j] < i:
                current_len -= 1
            elif stages[j] == i:
                failed += 1
        if failed == 0:
            temp.append((i, 0))
        else:
            failure_rate = failed / current_len
            temp.append((i, failure_rate))
    temp.sort(key=lambda x : x[1], reverse = True)
    for i in temp:
        answer.append(i[0])
    return answer
