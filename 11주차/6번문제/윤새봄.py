def solution(p):
    answer = ''
    
    def splitStr(str):
        left=0
        right=0
        for i in range(len(str)):
            if (str[i]=="("):
                left+=1
            else:
                right+=1
            if (left==right):
                return str[:i+1], str[i+1:] 
    
    def isCorrectStr(str):
        stack=[]
        for s in str:
            if (s=="("):
                stack.append(s)
            else:
                if(len(stack)==0):
                    return False
                else:
                    stack.pop()
        return True
    
    if (len(p)==0):  # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환.
        return answer
    
    u, v = splitStr(p) # 2. 문자열을 u,v로 반환함.
    
    if (isCorrectStr(u)): # 3. u가 올바른 문자열인 경우, v에 대해 1단계부터 다시 수행.
        answer += u
        answer += solution(v)
        return answer
    
    answer += "("   # 4. u가 올바른 문자열이 아닌 경우, 4-1 ~ 4-5수행.
    answer += solution(v)
    answer += ")"
    for i in range(1, len(u)-1):
        if (u[i]=="("):
            answer += ")"
        else:
            answer += "("
            
    return answer