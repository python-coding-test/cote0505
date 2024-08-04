'''
비손실 압축방법

aabbaccc는 2a2ba3c로 압축

문자열을 1개 이상의 단위로 잘라서 압축하자

ababcdcdababacdcd 를 2개 단위로 자르면
2ab2cd2ab2cd가 된다
8개 단위로 압축하면

2ababcdcd

압축해서 표현된 문자열의 길이 중 가장 짧은걸로


'''

s ="aaaaaaaaaabbbbbbbbbb"#"xababcdcdababcdcd"#"abcabcabcabcdededededede"#"ababcdcdababcdcd"


'''
abab cdcd abab cdcd


'''





result = 9

def solution(s):
    answer = len(s)*100

    for c in range(1,len(s)+1):
        temp = s[:c]
        cnt = 1
        result = len(s)
        
        for char in range(c, len(s)+c, c):
            #첫 c개의 문자와 그 다음 c개의 문자가 같으면 압축 가능
            # 3번 중복이라고 치면 1번만 쓰고 앞에 숫자 3 쓰면 되니까
            # cnt-1 개( 2회 반복 ) 삭제, 숫자 하나 앞에 추가 
            if temp == s[char: char+c]:
                cnt += 1
                
            else:
                if cnt != 1:
                    result -= (c*(cnt-1)-1)
                    if cnt>9:
                        result += len(str(cnt))-1
                        

                cnt = 1
                temp = s[char:char+c]

        if cnt > 1:
            result -= (c*(cnt-1)-1)
            if cnt>9:
                result += len(str(cnt))-1
        

        if answer > result:
            answer = result
    
    return answer


print(solution(s))
