'''
괄호 변환

짝이 안맞아

( ) 갯수가 같다 : 균형잡힌 괄호 문자열

( ) 괄호의 짝도 맞다 : 올바른 괄호 문자열

(()))( : 균형잡힌 괄호 문자열 + not 올바른 괄호 문자열

(())() : 둘다

w가 균형잡힌 괄호 문자열이라면 과정 통해 올바른 괄호 문자열로 변환 가능


균형 잡힌 p가 입력될 때 올바르게 고치기




'''
p ="(()())()"









def isbalanced(p):
    left = 0
    right = 0
    for s in range(len(p)) :
        if p[s] == '(':
            left += 1
        else:
            right += 1
        if left == right:
                return p[:s+1], p[s+1:]
        
  

def iscorr(p):
    value = 0

    for w in p:
        if w == '(':
            value += 1
        else:
            value -= 1
        if value < 0:
            return False
        
    return True


def solution(p):
    answer = ''
    
    if len(p)==0:
        return ''
    
    u, v = isbalanced(p)

    if iscorr(u):
        return  u + solution(v)
    
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for s in u[1:len(u)-1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('
            
        
            


    return answer


print(solution(p))
