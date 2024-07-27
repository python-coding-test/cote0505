import re

def solution(new_id):
    answer = ''
    
    def phase1(new_id):
        return new_id.lower()
    
    def phase2(new_id):
        return re.sub(r'[^a-z0-9-_.]','',new_id) 
    
    def phase3(new_id):
        return re.sub(r'\.{2,}','.',new_id)
            
    def phase4(new_id):
        return new_id.strip('.')
    
    def phase5(new_id):
        if len(new_id)==0:
            return "a"
        else:
            return new_id
        
    def phase6(new_id):
        if (len(new_id)>=16):
            new_id = new_id[:15]
        return new_id.rstrip('.')
    
    def phase7(new_id):
        while(len(new_id)<3):
            new_id+=new_id[-1]
        return new_id
    
    id = phase1(new_id)
    #print(id) # ...!@bat#*..y.abcdefghijklm
    id = phase2(id)
    #print(id) # ...bat..y.abcdefghijklm
    id = phase3(id)
    #print(id) # .bat.y.abcdefghijklm
    id = phase4(id)
    #print(id) # bat.y.abcdefghijklm
    id = phase5(id)
    #print(id)
    id = phase6(id)
    #print(id) # bat.y.abcdefghi
    id = phase7(id)
    #print(id)
    
    answer = id
    
    return answer