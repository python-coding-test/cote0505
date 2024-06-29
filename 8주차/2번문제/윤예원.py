from collections import deque
def solution(queue1, queue2):
    total = sum(queue1)+sum(queue2)
    if total %2 !=0:
        return -1
    target = total // 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    count = 0
    res1, res2 = sum(q1), sum(q2)
    while True:
        
        if res1 == target and res2 == target:
            print(count)
            return count
        if res1 < target:
            a = q2.popleft()
            if a > target:
                return -1
            q1.append(a)
            res2 -= a
            res1 += a
        elif res1 > target:
            a = q1.popleft()
            if a > target:
                return -1
            q2.append(a)
            res1 -= a
            res2 += a
        
        count+=1
        if count > 3 * len(queue1)-3:
            return -1
solution([1, 1, 1, 1], [1, 1, 7, 1])      