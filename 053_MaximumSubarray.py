class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        if len(nums) <=0:
            return 0;

        maxResult,curMax = nums[0], nums[0]

        for i in nums[1:]:
            curMax = max(i, (curMax+i))
            maxResult = max(curMax, maxResult)
        return maxResult

if __name__ == "__main__":
    solution = Solution()
    a = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(a)
