def solution(sequence, k):
    answer = []
    
    # 시간초과 발생.. -> 투포인터로 풀어야 함!
    start, end = 0, 0
    # seqeunce[start:end]와 k를 비교해서 포인터 위치를 +1 또는 -1 해줌.
    sum = sequence[0]
    min_len = 1000001
    
    while start<=end and end<len(sequence):
        if sum == k:
            if end-start+1 < min_len:
                min_len = end-start+1
                answer = [start, end]
            sum -= sequence[start]
            start += 1
        
        elif sum < k:
            end += 1
            if end < len(sequence):
                sum += sequence[end]

        elif sum > k:
            sum -= sequence[start]
            start += 1

    
    return answer