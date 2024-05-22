from collections import deque
def find_num(n):
    if n <= 10:
        return n-1
    queue = deque(range(1,10))
    count = 10 #이미 0~9까지 세었음
    while queue:
        num = queue.popleft()
        last_digit = num % 10
        for i in range(last_digit):
            new_num = num*10+i
            if new_num > 9876543210:
                return -1
            else:
                queue.append(new_num)
                print(new_num)
                count+=1
                if count == n:
                    return new_num
    return -1
n = int(input())
print(find_num(n))