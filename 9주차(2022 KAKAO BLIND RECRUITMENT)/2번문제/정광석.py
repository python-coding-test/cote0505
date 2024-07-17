'''
양의 정수 n 주어짐

숫자를 k진수로 바꾸면 변환된 수 안에 조건에 맞는 소수가 몇개인가

0p0

'''

import math
input_n = 110011#437674
input_k = 10

def is_prime_number(x):
    if x==1 : return False
    
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


def solution(n, k):
    answer = 0
    converted = ''
    while(n):
        n, mod = divmod(n, k)
        converted += str(mod)

    converted = converted[::-1]
    #print(converted)
    remove_zero = list(converted.split('0'))
    #print(remove_zero)

    for i in remove_zero:
        if i == '':
            continue
        if is_prime_number(int(i)):
            answer +=1
        

    return answer





print(solution(input_n,input_k))
