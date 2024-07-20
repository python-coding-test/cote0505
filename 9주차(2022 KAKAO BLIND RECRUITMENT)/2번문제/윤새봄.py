def isPrime(n):
    if (n<2):
        return False
    for i in range(2, int(n**0.5)+1):
        if (n%i==0):
            return False
    return True
        

def solution(n, k):
    answer = 0
    
    # 1. n을 k진수로 바꾼다.
    arr = []
    while (n!=0):
        arr.append(n%k)
        n = n//k
    
    res = 0
    for i in range(len(arr)-1, -1, -1):
        res = res*10 + arr[i]
    # print(res)
    
    # 2. 0P0, P0, 0P, P 찾는다.
    for part in str(res).split('0'):
        if (part):
            p = int(part)
            if isPrime(p):
                answer += 1
        
    return answer