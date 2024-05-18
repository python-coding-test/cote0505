import math, sys
input = sys.stdin.readline
a,b = map(int, input().split())

def countnum(n): #소수가 아닌 것의 개수
    if  n<= 1:
        return 0
    else:
        arr_val = set()
        for i in range(2, int(math.sqrt(n))+1):        
            j = 2
            while i*j <= n:
                arr_val.add(i*j)
                j+=1
        return len(arr_val)


count_val = b - (countnum(b) - countnum(a)) -2

print(count_val)




