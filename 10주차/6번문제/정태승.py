from collections import deque

def solution(new_id):
    
    # 1단계
    new_id = new_id.lower()
    
    
    # 2단계
    new_id_2 = ''
    for n in new_id:
        if ord('a') <= ord(n) <= ord('z') or ord('0') <= ord(n) <= ord('9') or n == '-' or n == '_' or n == '.':
            new_id_2 += n
    # print(new_id_2)
    
    # 3단계
    prev = 0
    new_id_3 = ''
    for i in range(1, len(new_id_2)):
        if new_id_2[prev] == '.' and new_id_2[i] == '.':
            prev = i
            continue
        
        new_id_3 += new_id_2[prev]
        prev = i
    
    new_id_3 += new_id_2[prev]
            
    
    new_id_4 = deque(list(new_id_3))
    
    # print(new_id_4)
    
    # 4단계
    if new_id_4 and new_id_4[-1] == '.':
        new_id_4.pop()
        
    if new_id_4 and new_id_4[0] == '.':
        new_id_4.popleft()
    
    # print(new_id_4)
    
    # 5단계
    if not new_id_4 :
        new_id_4.append('a')
    
    # 6단계
    new_id_4 = list(new_id_4)
    if len(new_id_4) >= 16:
        new_id_4 = new_id_4[:15]
        
    if new_id_4[-1] == '.':
        new_id_4.pop()
    
    # print(new_id_4)
    
    # 7단계
    if len(new_id_4) <= 2:
        while len(new_id_4) < 3:
            new_id_4.append(new_id_4[-1])
    
    answer = ''.join(new_id_4)
    
    return answer




# 다른 풀이
# def solution(new_id):
#     answer = ''
#     # 1
#     new_id = new_id.lower()
#     # 2
#     for c in new_id:
#         if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
#     # 3
#     while '..' in answer:
#         answer = answer.replace('..', '.')
#     # 4
#     if answer[0] == '.':
#         answer = answer[1:] if len(answer) > 1 else '.'
#     if answer[-1] == '.':
#         answer = answer[:-1]
#     # 5
#     if answer == '':
#         answer = 'a'
#     # 6
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
#     # 7
#     while len(answer) < 3:
#         answer += answer[-1]
#     return answer
