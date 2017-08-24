def twoSum(nums, target):
    dictResult = {}
    for i in range (0,len(nums)):
        complement = target - nums[i]
        if complement in dictResult.keys():
            return complement, nums[i]
        dictResult[nums[i]]=i

if __name__ == "__main__":
    nums = [1,3,4,5,6,7]
    tar  = 10
    a , b = twoSum(nums, tar)

    print(a)
    print(b)

