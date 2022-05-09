def solution(priorities, location): #[2, 1, 3, 2], 2
  
    # stack = [0] * len(priorities)
    # stack[location] = 'key' #['key',0,0,0]
    stack = [c for c in range(len(priorities))]

    i = 0

    while True:#가장 앞에 있는게 제일 큰 수 일때까지    
        if priorities[i] < max(priorities[i+1:]): 
            #앞에 뽑은 front값보다 큰값이 대기순번 안에 있을 경우
            priorities.append(priorities.pop(i))    
            stack.append(stack.pop(i))
            continue
        else:   #앞에 뽑은 front값이 대기순번에서 가장 큰값인 경우
            i += 1

        if priorities == sorted(priorities,reverse = True):    
            break
    
    return stack.index(location) + 1


# prior = [2,3,1,2] # ->
# loc = 0

# print(solution(prior,loc))
