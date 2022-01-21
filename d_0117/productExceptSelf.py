from itertools import product

def productExceptSelf(nums): #[1,2,3,4]
    list = []
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    for i in range(len(nums)):
        sudolist = nums.copy()
        list.append(multiplylist(sudolist,i))
    return list
    
def multiplylist(numbers,num): #해당 인덱스 삭제 후 나머지 곱
    numbers.pop(num)
    a = 1
    for i in numbers:
        a *= i
    return a    

anums = [1,2,3,4]
print(productExceptSelf(anums))      