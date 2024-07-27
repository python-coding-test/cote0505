import math

def check(num):
    if num == 1:
        return 0
    for i in range(2,int(math.sqrt(num)+1)):
        if not num%i:
            return 0
    return 1

def solution(n, k):
    temp = ''
    while n:
        temp += str(n%k)
        n //= k

    cnt = 0
    for i in temp[::-1].split('0'):
        if i == '':
            continue
        cnt += check(int(i))

    return cnt