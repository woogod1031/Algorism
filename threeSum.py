#[-1,0,1,2,-1,-4]
def SumNum(nums):
    nums.sort()

    result = []
    nums2 = []
    nums3 = []

    for i in range(len(nums)): # -4,-1,-1,0,1,2
        #print(i)
        if nums[i] == nums[i-1]: #sort로 정렬을 시켰을 때 중복되는 값은 
                                 #피하기 위해 이전에 계산한 값과 동일한 경우 continue
            continue
        if len(nums) - i <= 2: #i의 마지막위치
            continue
        nums2 = nums[i+1:]
        for j in range(len(nums2)):
            #print(j)
            if nums2[j] == nums2[j-1]: #sort로 정렬을 시켰을 때 중복되는 값은 피하기 위해
                continue
            if len(nums2) - j <= 1: #j의 마지막위치
                continue
            nums3 = nums2[j+1:]
            for k in range(len(nums3)):
                #print(k)
                result_num = nums[i] + nums2[j] + nums3[k]
                if  result_num == 0:                                                        
                    result.append([nums[i], nums2[j], nums3[k]])                
                    #print("yes")                
    return result                      

numlist = [-1,0,1,2,-1,-4,-5,5]
#[-4,-1,-1,0,1,2]
print(SumNum(numlist))






# class Solution:
#     #[-1,0,1,2,-1,-4]
#     def threeSum(self,nums):
#         nums.sort()
    
#         result = []
#         nums2 = []
#         nums3 = []
    
#         for i in range(len(nums)): # -1,0,1,2,-1,-4
#             #print(i)
#             if nums[i] == nums[i-1]:
#                 continue
#             if len(nums) - i <= 2:
#                 continue
#             nums2 = nums[i+1:]
#             for j in range(len(nums2)):
#                 #print(j)
#                 if nums2[j] == nums2[j-1]:
#                     continue
#                 if len(nums2) - j <= 1:
#                     continue
#                 nums3 = nums2[j+1:]
#                 for k in range(len(nums3)):
#                     #print(k)
#                     result_num = nums[i] + nums2[j] + nums3[k]
#                     if  result_num == 0:                                                        
#                         result.append([nums[i], nums2[j], nums3[k]])                
#                         #print("yes")                
#         return result                      
    
 

