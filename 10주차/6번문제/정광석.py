'''
규칙 안맞으면 유사하면서 규칙에 맞는 아이디 추천

알파벳 소문자, 숫자, - _ . 만 사용 가능

. 는 맨앞 맨 뒤에 사용 불가, 연속 사용 불가


7 단계 순차 처리 과정

new_id 가 입력되면

1. 대문자 -> 소문자
2. 소문자, 숫자 - _ . 제외하고 모두 제거
3. . 2번 이상 연속되면  . 하나로 치환
4. . 가 맨 앞 맨 뒤면 제거
5. 빈 문자열이면 "a" 대입
6. 16자 이상이면, new_id 첫 15개 제외한 나머지 문자 제거
    제거 하고 나서 맨 뒤에  . 있으면 제거
7. 2자 이하라면 마지막 문자를 3이 될 때 까지 반복해서 끝에 붙임
'''

new_id = 	"123_.def"#"z-+.^."#"...!@BaT#*..y.abcdefghijklm"


def solution(new_id):
    answer = ''

    #1 대소문자 변환
    new_id = new_id.lower()
    #print(new_id)

    #2 규칙 안맞는거 제거
    allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyz-_.")
    new_id = ''.join([s for s in new_id if s in allowed_chars])
        
    #3 . 2번 중복 제거
    stack = ''
    prev= ''
    for s in new_id:
        if s=='.' and prev == '.':
            continue
        stack += s
        prev = s

    new_id = stack
    #print(new_id)
    #4. . 맨앞 맨뒤 제거
    if new_id[0] == '.' :
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.' :
        new_id = new_id[:-1]
    #print(new_id)

    #5. 빈 문자열이면 "a" 대입
    if len(new_id) == 0 :
        new_id = "a"

    #print(new_id)


    #6. 16자 이상이면 제거
    if len(new_id)>=16:
        new_id = new_id[:15]
    if new_id[0] == '.' :
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.' :
        new_id = new_id[:-1]

    #print(new_id)

    #7. 2자 이하라면 마지막 문자를 3개 될때까지 반복
    add = new_id[-1]
    if 0<=len(new_id)<=2: 
        while len(new_id)<=2:
            new_id += add
            
    #print(new_id)
    #print(len(new_id))
    return new_id

solution(new_id)
