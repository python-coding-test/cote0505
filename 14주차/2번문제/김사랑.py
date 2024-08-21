"""
44.1/100
1번 테케 틀림
반 이상 시간초과
"""

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
