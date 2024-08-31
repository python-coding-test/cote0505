#gpt 참조한 코드입니다

import copy

def rotate_clock(grid, r, c):
    n = len(grid)
    # 현재 시계와 상하좌우 시계를 90도씩 회전
    grid[r][c] = (grid[r][c] + 1) % 4
    if r > 0:
        grid[r-1][c] = (grid[r-1][c] + 1) % 4
    if r < n - 1:
        grid[r+1][c] = (grid[r+1][c] + 1) % 4
    if c > 0:
        grid[r][c-1] = (grid[r][c-1] + 1) % 4
    if c < n - 1:
        grid[r][c+1] = (grid[r][c+1] + 1) % 4

def is_solved(grid):
    return all(grid[r][c] == 0 for r in range(len(grid)) for c in range(len(grid)))

def solution(clockHands):
    n = len(clockHands)
    min_operations = float('inf')

    # 첫 번째 행의 각 시계에 대해 0, 1, 2, 3번 회전하는 경우의 수를 모두 시도
    for first_row in range(4 ** n):
        current_grid = copy.deepcopy(clockHands)
        operations = 0

        # 첫 번째 행의 상태 설정
        for c in range(n):
            rotations = (first_row // (4 ** c)) % 4
            for _ in range(rotations):
                rotate_clock(current_grid, 0, c)
            operations += rotations

        # 첫 번째 행을 기준으로 나머지 행들 처리
        for r in range(1, n):
            for c in range(n):
                if current_grid[r-1][c] != 0:  # 위쪽 시계가 12시 방향이 아닐 때
                    rotations = 4 - current_grid[r-1][c]
                    for _ in range(rotations):
                        rotate_clock(current_grid, r, c)
                    operations += rotations

        # 모든 시계가 12시를 가리키는지 확인
        if is_solved(current_grid):
            min_operations = min(min_operations, operations)

    return min_operations