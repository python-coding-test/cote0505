def solution(sequence, k):
    s,e = 0,0
    cur_sum = sequence[0]

    res = [s,e]
    minLength = len(sequence)
    while e < len(sequence):
        if cur_sum < k:
            e += 1
            if e < len(sequence):
                cur_sum += sequence[e]

        elif cur_sum > k:
            cur_sum -= sequence[s]
            s += 1

        else:
            if (e-s) < minLength:
                minLength = e-s
                res = [s,e]
            cur_sum -= sequence[s]
            s += 1

    return res