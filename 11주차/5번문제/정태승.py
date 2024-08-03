def solution(s):
    answer = float('inf')
    
    def concat(n):
        st = []
        ans = ''
        for i in range(0, len(s), n):
            tmp = s[i:i+n]
            if not st:
                st.append(tmp)
            elif st[-1] != tmp:
                if len(st) != 1:
                    ans += str(len(st))    
                ans += st[-1]
                st = []
                st.append(tmp)
            else:
                st.append(tmp)
        
        if st :
            if len(st) != 1:
                ans += str(len(st))
            ans += st[-1]
            
        return len(ans)
            
    if len(s)==1:
        return 1
    
    for n in range(1, len(s)):
        answer = min(answer, concat(n))
    
    return answer