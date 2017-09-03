class Solution(object):
    def twoSum(nums, target):
        dictResult = {}
        for i in range (0,len(nums)):
            complement = target - nums[i]
            if complement in dictResult.keys():
                return dictResult[complement],i
            dictResult[nums[i]]=i

if __name__ == "__main__":
    nums = [3,2,4]
    tar  = 6
    solution = Solution
    a , b = solution.twoSum(solution, nums, tar)
    print(a)
    print(b)