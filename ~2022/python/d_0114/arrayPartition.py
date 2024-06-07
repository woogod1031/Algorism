#[1,4,3,2]
def arrayPartition(nums):
    result = 0
    nums.sort() #[1,2,3,4]
    for i in range(len(nums)):
        if i % 2 == 0:  #인덱스 i가 짝수인 경우(min(a,b)에서 a에 위치)
            if i is not len(nums)-1: #짝수 위치면서 마지막에 위치한 인덱스 예외 => len(num)이 홀수인 경우 
                result += nums[i]
            else:
                continue

    return result

numbers = [1,4,3,2,5,7,8] #1,2,3,4,5,7,8
print(arrayPartition(numbers))          



