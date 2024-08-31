# '''
# 동전 뒤집기, 모든 동전 앞뒤 구분됨
# 동전 뒤집을 때 같은 줄 모든 동전 뒤집어야 함

# 초기, 목표가 주어졌을 때 초기에서 


# '''

beginning,	target,	result = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],	[[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]],	5


# def solution(beginning, target):
#     answer = 0
#     n = len(beginning)
#     temp = [[0]*n for _ in range(n)]
#     def a_print(arr):
#         for i in arr:
#             for j in i:
#                 print(j, end='')
#             print()
#     for i in range(len(temp)):
#         for j in range(len(temp[0])):
#             if beginning[i][j] == target[i][j]:
#                 temp[i][j] = 0
#             else:
#                 temp[i][j] = 1
#     a_print(temp)

#     return answer


# solution(beginning,target)

def flip_row(matrix, row_index):
    matrix[row_index] = ['1' if x == '0' else '0' for x in matrix[row_index]]

def flip_col(matrix, col_index):
    for i in range(len(matrix)):
        matrix[i][col_index] = '1' if matrix[i][col_index] == '0' else '0'

def count_ones(matrix):
    return sum(row.count('1') for row in matrix)

def solution(beginning, target):
    n = len(beginning)
    temp = [[0]*n for _ in range(n)]
    answer = []
    
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if beginning[i][j] == target[i][j]:
                temp[i][j] = 0
            else:
                temp[i][j] = 1
    
   


print(solution(beginning, target))

