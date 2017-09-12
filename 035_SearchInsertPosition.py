from math import fabs
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) ==0 or nums ==None:
            return 0
        elif target < nums[0]: return 0
        elif target > nums[len(nums)-1]: return len(nums)
        if target not in nums:
            a = list(map(lambda x: fabs(x - target), nums))
            x = a.index(min(a))
            if target < nums[x]:return x
            else: return x+1
        else:
            return nums.index(target)

if __name__ == "__main__":
    solution = Solution
    a = solution.searchInsert(solution, [1,3,5,6],0)
    print(a)