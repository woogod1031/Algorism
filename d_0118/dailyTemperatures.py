from calendar import prweek

def dailyTemperatures(temperatures):
    result = [0] * len(temperatures) #인덱스로 구성할 예정
    stack = []

    for index, temp in enumerate(temperatures): #index,temp

        while stack and temp > temperatures[stack[-1]]:

            prev = stack.pop()    

            result[prev] = index - prev 

        stack.append(index)

    return result
         
input = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(input))    
#result = 1,1

        



            
             

            




weather = [5,6,7,3,2,4,8,5]

assert dailyTemperatures(weather)

            





    



temperatures = [73,74,75,71,69,72,76,73]
assert dailyTemperatures(temperatures)