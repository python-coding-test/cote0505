# def rotate_key(key):
#     return list(zip(*key[::-1]))

# def check(lock, lock_length):
#     for i in range(lock_length, lock_length*2):
#         for j in range(lock_length, lock_length*2):
#             if lock[i][j] != 1:
#                 return False
#     return True

# def solution(key, lock):
#     lock_length = len(lock)
#     key_length = len(key)

#     # 여백 - 자물쇠 - 여백 => 3배 크기
#     new_lock = [[0] * (lock_length*3) for _ in range(lock_length*3)]

#     # 자물쇠 가운데 위치시키기
#     for i in range(lock_length):
#         for j in range(lock_length):
#             new_lock[i+lock_length][j+lock_length] = lock[i][j]

#     for rotation in range(4):
#         key = rotate_key(key)
#         for x in range(lock_length*2):
#             for y in range(lock_length*2):
#                 # 열쇠 넣기
#                 for i in range(key_length):
#                     for j in range(key_length):
#                         new_lock[x+i][y+j] += key[i][j]
#                 # 자물쇠가 맞는지 검사
#                 if check(new_lock, lock_length):
#                     return True
#                 # 열쇠 빼기
#                 for i in range(key_length):
#                     for j in range(key_length):
#                         new_lock[x+i][y+j] -= key[i][j]
#     return False

def rotateKey(key):
    return list(zip(*key[::-1]))

def isFullLock(newLock, originLockLength, keyLength):
    for i in range(originLockLength):
        for j in range(originLockLength):
            if newLock[i+keyLength-1][j+keyLength-1] != 1:
                return False
    return True

def releaseLock(key, lock, sx, sy):
    for i in range(len(key)):
        for j in range(len(key)):
            lock[i+sx][j+sy] += key[i][j]

    return lock

def initNewLock(newLock, lock, keyLength):
    for i in range(len(lock)):
        for j in range(len(lock)):
            newLock[i+keyLength-1][j+keyLength-1] = lock[i][j]

def check(rotate,lock):
    print(rotate+1,"번째 회전")
    for i in lock:
        print(i)


def solution(key, lock):
    newLength = len(lock) + 2*(len(key)-1)
    newLock = [[0]*newLength for _ in range(newLength)]
    initNewLock(newLock, lock, len(key))

    for i in range(len(newLock)- len(key) -1):
        for j in range(len(newLock) - len(key) -1):
            for k in range(4):
                rotateKey(key)
                releaseLock(key, newLock, i, j)
                res = isFullLock(newLock, len(lock), len(key))
                if res:
                    return True
                check(k,newLock)
                initNewLock(newLock, lock, len(key))
    return False

res = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
print(res)