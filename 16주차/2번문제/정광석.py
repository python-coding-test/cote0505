    def find_parent(parent,a):
    temp_list = [0]
    while True:
        temp_list.append(a)
        
        if a==parent[a]:
            break
        a = parent[a]
    return temp_list






def main():

    t = int(input())
    
    for __ in range(t):
        n = int(input())
        parent = [i for i in range(n+1)]
        
        #print(parent)
        for _ in range(n-1):
            a,b = map(int, input().split())
            parent[b] = a

             
        
        target_a, target_b = map(int, input().split())
        target_a_parent = find_parent(parent, target_a)
        target_b_parent = find_parent(parent, target_b)
        # print(target_a_parent)
        # print(target_b_parent)
        # print(parent)
        answer = 0
        i = 1
        while True:
            if target_a_parent[-i] != target_b_parent[-i]:
                answer = target_a_parent[-i+1]
                break
            else:
                i+=1
        # print(parent)
        print(answer)


        


main()