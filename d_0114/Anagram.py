#input a = ["eat","tea","tan","ate","nat","bat" ]

# def isAnagram(array):
   
#     func_array = []

#     for i in range(len(array)): #6개 뽑아냄
#         str = []
#         print(i)
#         print(array[i])
#         if len(func_array) == 0: #첫번째 단어있지 체크
#             func_array.append(array[i])
#             continue
#         for j in range(len(array[i])): #개당 문자 3개씩 뽑아냄                                                      
#             if array[i][j] in func_array[i-1]:
#                 print("yes")
#             else:
#                 func_array
import collections
from typing import List


def groupAnagrams(strs): 
    dic = {} #"eat", "tea", "tan", "nta" ,"ate", "nat", "bat", "tba"
    for word in strs:   # word.sort -> 반환값 없음 
                        # sorted(word) -> 정렬된 문자열을 반환 
                        #ex)a="apple" -> sorted(a) -> ['a', 'e', 'l', 'p', 'p']
        key = "".join(sorted(word)) # ['a', 'e', 't'] => 'aet' 
        if key not in dic.keys(): #지금 만든게 dic의 key중에 있는가
            dic[key] = [word] #value에 배열[]을 생성 
        else: dic[key].append(word) #value 배열[]에 값을 추가
        # print(dic) 
    return list(dic.values()) #value값(배열)만 리턴


#strs : List[str] 해당 형식
#-> List[List[str]]: 이거의 뜻은 이 함수가 반환해주는 값의 형식이 List[List[str]]라는 것을 말한다!
#def groupAnagramss(strs: List[str]) -> List[List[str]]: 
def groupAnagramss(strs): 
    dic = collections.defaultdict(list) #dictionary 생성
    #"eat", "tea", "tan", "nta" ,"ate", "nat", "bat", "tba"
    for word in strs:
        key = "".join(sorted(word))
        dic[key].append(word) #위랑 다르게 배열을 생성x, 바로 값 입력과 동시에 생성
    return list(dic.values())
 
strs = ["eat", "tea", "tan", "nta" ,"ate", "nat", "bat", "tba"] 
 
print(groupAnagrams(strs))
print(groupAnagramss(strs))


# a = []
# b=[1,2,3]
# c=[1,2,3]
# d=[1,2,3]
# a.append(b)
# a.append(c)
# a.append(d)
# a[0].append(4)
# print(a)

# a = ["eat"]
# def groupAnagrams(array):
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i]


#def groupAnagrams(strs): 

                
                

            

#isAnagram(["eat","tea","tan","ate","nat","bat"])          

    
