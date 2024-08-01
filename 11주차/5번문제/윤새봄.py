def solution(s):
    answer = 1001
    if (len(s)==1): # 테스트 5 계속 실패된 원인.
        answer=1
    for gap in range(1, len(s)//2 + 1):
        compressed = ""
        stack = []
        #print(f"gap : {gap}")
        for j in range(0, len(s), gap):
            word = s[j:j+gap]
            #print(f"word : {word}")
            if (len(stack)==0):
                stack.append(word)
            else:
                if (stack[-1]==word):
                    stack.append(word)
                else:
                    if (len(stack)!=1): # 문자가 반복되지 않아 한번만 나타나는 경우 1은 생략.
                        compressed+=str(len(stack))
                    compressed+=stack[-1]
                    stack=[word]
            #print(f"compressed : {compressed}")
        if (len(stack)!=1):
            compressed+=str(len(stack))
        compressed+=stack[-1]
        #print(f"final compressed : {compressed}")
        if (len(compressed)<answer):
            answer=len(compressed)
    return answer