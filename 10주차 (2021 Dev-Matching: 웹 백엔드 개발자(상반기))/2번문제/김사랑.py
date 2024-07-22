'''
코드 최적화
'''
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]  # 인덱스 0부터 6까지의 순위 (일치하는 숫자 개수에 따른 순위)

    count_win = sum(1 for i in lottos if i in win_nums)
    count_zero = sum(1 for i in lottos if i == 0)

    max_rank = rank[count_win + count_zero]
    min_rank = rank[count_win]

    return [max_rank, min_rank]

'''
처음 푼 방식
'''
# def solution(lottos, win_nums):
#     answer = []
#     rank = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2}  # 순위, 당첨 일치 개수
#     count_win = 0
#     count_zero = 0
#     max_rank = 6
#     min_rank = 6

#     for i in lottos:
#         if i in win_nums:
#             count_win += 1
#         if i == 0:
#             count_zero += 1

#     for a, b in rank.items():
#         if b == count_win+count_zero:
#             max_rank = a

#     for a, b in rank.items():
#         if b == count_win:
#             min_rank = a
        
#     answer.append(max_rank)
#     answer.append(min_rank)
    
#     return answer
