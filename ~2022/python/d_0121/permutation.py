# class Solution(object):
def permute(self, nums): #[1,2,3]
    result = []
    prev_elements = []
    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements.copy())
        pass

        for e in  elements: #[1,2,3]
            next_elements = elements[:] #값만을 가져와야 하기 때문, elements만 넣으면 ele값이 변경되면 다른값도 변경됨
            # next_ ele mentss => 1,2,3
            next_elements.remove(e) #2,3

            prev_elements.append(e) #1
            dfs(next_elements)
            prev_elements.pop() 



    dfs(nums) #[1,2,3]
    pass

######################
def letterCombinations(self, digits): #236 총 세자리 숫자        
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
                
            for i in range(index, len(digits)): #세번을 돌려야 한다.
                #숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]: #digits 236의 i번째 값을 key로 하여 dict에서 string value를 가져온다
                    #ex) dic[digits[0]] => dic[2]의 value값 => 'abc'를 나누어 보낸다
                    dfs(i + 1, path + j)
        
        if not digits:
            return []
        
        dic = { 
             '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
             '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'
         }
    
        result = []    
        dfs(0,"")
        
        return result
        