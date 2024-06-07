def solution(progresses, speeds):
          #[93,30,55] [1, 30, 5]
    answer = [] #result
    stack = []
    count = 0

    for i in range(len(progresses)): #[93,30,55]
        
        while progresses[i] < 100: #100이상이 되면 while문을 빠져나간다 
            count += 1 #9
            if speeds[i] == 0:
                 count = 0
                 break                
            progresses[i] += speeds[i]  
            
        if stack and count <= max(stack): #가장 최근값이 아닌 max값
            stack.append(count) 
            count = 0        
            continue
        elif stack and count > max(stack):
            answer.append(len(stack))
            stack.clear()
            stack.append(count)
            count = 0 
            continue

        if progresses[i] == progresses[-1]: #마지막인지
            answer.append(1)
            count = 0 
            continue
             
        stack.append(count)    #7,3
        count = 0

    answer.append(len(stack))
        
    

    return answer    

pg = [55, 60, 65] 
sp = [5, 10, 7] # =>3
print(solution(pg,sp))