import collections

def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    sq = 0
    while q:
        sec+=1
        temp1 = q.pop(0)
        if temp1 != 0:
            sq += temp1
            pass
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
                temp2 = truck_weights.pop(0)
            else:
                q.append(0)
    return sec

bl = 2
we = 10 # =>3
tw = [7,4,5,6] # =>3
print(solution(bl,we,tw))