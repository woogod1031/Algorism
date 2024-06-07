# input : num = [2,7,11,15]
#target : 9
# output : [0,1] (list)]

#브루트포스(완전탐색, 완전 매칭)

def twoSum(nums, target):
    for i,n in enumerate(nums):
        complement = target - n

        if complement in nums[i +1:]:
            return [nums.index(n), nums[i + 1:]].index(complement) + (i + 1)   