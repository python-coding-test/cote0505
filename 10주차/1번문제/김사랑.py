# 사라지는 발판

'''
dfs, 백트래킹으로 구현
'''

def solution(board, aloc, bloc):
    # answer = -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def dfs(board, aloc, bloc):
        x, y = aloc  # 현재 플레이어의 위치

        rows = len(board)
        cols = len(board[0])

        if board[x][y] == 0:
            return False, 0  # 현재 위치가 이미 사라졌다면 패배

        # 현재 가능한 최대/최소 이동 거리와 승리 여부 초기화
        max_v = 0
        min_v = float('inf')
        isWin = False

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 1:
                board[x][y] = 0  # 방문 처리

                # 상대방의 위치로 dfs 호출하여 결과 획득
                opponent_isWin, step = dfs(board, bloc, (nx, ny))

                step += 1  # 이동 횟수 증가
                board[x][y] = 1  # 원상 복귀

                # 상대방이 이기지 못하는 경우
                if not opponent_isWin:
                    isWin = True
                    min_v = min(min_v, step)
                # 상대방이 이기는 경우
                else:
                    max_v = max(max_v, step)

        # 현재 플레이어가 이길 수 있는 경우 최소 이동 횟수 반환
        if isWin:
            return True, min_v

        # 현재 플레이어가 이길 수 없는 경우 최대 이동 횟수 반환
        else:
            return False, max_v

    # dfs가 반환하는 값은 2개인데, isWin은 필요없으므로 "_"로 표기
    _, answer = dfs(board, aloc, bloc)

    return answer


board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]
# 출력: 5

board1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
aloc1 = [1, 0]
bloc1 = [1, 2]
# 출력: 4

board2 = [[1, 1, 1, 1, 1]]
aloc2 = [0, 0]
bloc2 = [0, 4]
# 출력: 4

board3 = [[1]]
aloc3 = [0, 0]
bloc3 = [0, 0]
# 출력: 0

print(solution(board, aloc, bloc))
print(solution(board1, aloc1, bloc1))
print(solution(board2, aloc2, bloc2))
print(solution(board3, aloc3, bloc3))
