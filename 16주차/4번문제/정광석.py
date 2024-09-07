from itertools import product

def solution(clockHands):
    n = len(clockHands)

    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]

    def rot(state, y, x, num):
        for i in range(5):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < n and 0 <= tx < n:
                state[ty][tx] = (state[ty][tx] + num) % 4

    min_cnt = 10000000
    for cmb in product(range(4), repeat=n):
        state = [row[:] for row in clockHands]
        cnt = 0

        for i, num in enumerate(cmb):
            if num != 0:
                rot(state, 0, i, num)
                cnt += num

        for y in range(1, n):
            for x in range(n):
                if state[y-1][x] != 0:
                    num = (4 - state[y-1][x]) % 4 
                    rot(state, y, x, num)
                    cnt += num

       
        if state[n-1] == [0] * n:
            min_cnt = min(min_cnt, cnt)

    return min_cnt


clockHands = [[0, 1, 3, 0],
              [1, 2, 0, 0],
              [3, 0, 2, 2],
              [0, 2, 0, 0]]

print(solution(clockHands))
