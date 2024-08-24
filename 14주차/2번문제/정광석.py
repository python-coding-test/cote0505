'''

비 내림차순 정렬된 수열

기존 수열에서 임의의 두 인덱스의 원소와 그 사이 원소를 모두 포함하는 부분 수열

부분 수열의 합은 k

합이 k인 부분 수열이 여러개면 짧은거 찾기

길이가 짧은 수열 여러개면 앞쪽걸 찾기



합이 k 인 연속된 부분수열의 인덱스 찾는데 가장 짧은 수열을 찾고, 짧은게 여러개면 앞에걸 찾기


k 범위가 너무 크다
sequence 길이도 너무 길다

비 내림차순이면 오름차순(중복 가능)

for문으로 찾기는 어려울 듯



'''
sequence,	k,	result=[2, 2, 2, 2, 2]	,6	,[0, 2]#[1, 1, 1, 2, 3, 4, 5],	5,	[6, 6]



# '' 시간초과 '' 
# def solution(sequence, k):
#     answer = []
#     cnt = 1
#     start = 0
#     end = 0
#     flag =0
#     while True:        
        
#         if flag: break
#         for i in range(0,len(sequence)):
#             temp = sum(sequence[i:i+cnt])
            
#             #print(temp, sequence[i:i+cnt])
            
#             if temp == k:
#                 start = i
#                 end = i+cnt-1
#                 answer.append(start)
#                 answer.append(end)
#                 flag= 1
#                 break
        
#         cnt+=1
    
#     #print(sequence)
#     #print(cnt)
   
#     return answer


def solution(sequence, k):
    n = len(sequence)
    start, end = 0, 0
    current_sum = sequence[0]
    min_length = float('inf')
    answer = []

    while start < n and end < n:
        if current_sum == k:
            if end - start < min_length:
                min_length = end - start
                answer = [start, end]
            elif end - start == min_length and start < answer[0]:
                answer = [start, end]
            
            current_sum -= sequence[start]
            start += 1
        
        elif current_sum < k:
            end += 1
            if end < n:
                current_sum += sequence[end]
        
        else:  # current_sum > k
            current_sum -= sequence[start]
            start += 1

    return answer

sequence = [2, 2, 2, 2, 2]
k = 6
print(solution(sequence, k))  # [0, 2]
