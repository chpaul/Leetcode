class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nlen = len(nums)
        for i in range(len(nums)):
            while  0 < nums[i] <= nlen and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(nlen):
            if i != nums[i]-1: return i+1
        return  nlen+1


if __name__ == "__main__":
    solution = Solution()
    a = solution.firstMissingPositive([3,4,-1,1])
    print(a)