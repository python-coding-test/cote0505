import math

def solution(n, k):
    answer = 0
    n_to_k = ""
    
    def isPrime(p):    
        if p == 1 :
            return False
        if p == 2 :
            return True
        
        for i in range(2, int(math.sqrt(p))+1):
            if p%i == 0:
                return False
        return True

    
    while n > k:
        n_to_k = str(n%k) + n_to_k
        n//=k
    n_to_k = str(n) + n_to_k
    
    for l in list(n_to_k.split('0')):
        if l != '' :
            if isPrime(int(l)):
                answer+=1
    
    return answer