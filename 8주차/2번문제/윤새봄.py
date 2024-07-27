from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    count = 0
    while (sum1!=sum2):
        if (sum1>sum2):
            num = q1.popleft()
            q2.append(num)
            sum1-=num
            sum2+=num
        else:
            num=q2.popleft()
            q1.append(num)
            sum1+=num
            sum2-=num
        count+=1
        
        # queue1의 원소가 queue2로 전부 이동하고, queue2의 원소만 queue1으로 이동하고, 남은 queue2의 원소가 queue1으로 이동하는 경우.
        if (count > len(queue1)*3):
            return answer
    answer = count
    
    return answer