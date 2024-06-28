#https://school.programmers.co.kr/questions/64197
def solution(numbers):
    def check(i,s):
        L = len(s)//2
        if L:
            if s[L] == "0" and ('1' in s):
                numbers[i] = 0
            else:
                check(i, s[:L]), check(i, s[L+1:])
        
    for i, num in enumerate(numbers):
        s, numbers[i] = bin(num)[2:], 1
        len_s, L = len(s), 1 
        while len_s >= L:
            L*=2
        s = s.rjust(L-1, "0")
        check(i,s)
    return numbers