import sys

N, M = map(int, input().split())
train = {i+1:set() for i in range(N)}

def movePeople(type, param):
    trainIdx = param[0]
    if type == 1:
        train[trainIdx].add(param[1])
    elif type == 2:
        if param[1] in train[trainIdx]:
            train[trainIdx].remove(param[1])
    elif type == 3:
        if 20 in train[trainIdx]:
            train[trainIdx].remove(20)
        train[trainIdx] = set(map(lambda x: x+1, train[trainIdx]))
    else:
        if 1 in train[trainIdx]:
            train[trainIdx].remove(1)
        train[trainIdx] = set(map(lambda x:x-1, train[trainIdx]))

for _ in range(M):
    order = list(map(int, sys.stdin.readline().split()))
    movePeople(order[0], order[1:])

res = []
for i in train.values():
    if i in res:
        continue
    res.append(i)
print(len(res))