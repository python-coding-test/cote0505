"""
ref: https://studyoon.tistory.com/226
"""

def solution(sequence, k):
    answer = []
    end = 0
    sums = 0
    min_v = 1e9
    
    for start in range(len(sequence)):
        while end < len(sequence) and sums < k:
            sums += sequence[end]
            end += 1
        if sums == k:
            if min_v > (end-start):
                answer = [start, end-1]
            min_v = min(min_v, end-start)
        sums -= sequence[start]
    return answer



"""
기존 풀이

44.1/100
1번 테케 틀림
반 이상 시간초과


def solution(sequence, k):
    answer = []
    min_diff = float('inf')
    min_diff_array = None
    
    for i in range(len(sequence)):
        temp = sequence[i]
        if temp == k:
            answer.append([i,i])
            break
        for j in range(i+1, len(sequence)):
            if temp == k:
                answer.append([i,j-1])
                break
            elif temp > k:
                break
            else:
                temp += sequence[j]
    # print(answer)

    for i in answer:
        diff = i[1]-i[0]
        if diff < min_diff:
            min_diff = diff
            min_diff_array = i
        
    return min_diff_array

    """

