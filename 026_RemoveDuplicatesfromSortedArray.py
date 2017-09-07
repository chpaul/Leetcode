class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) ==0 : return []
        pntSlow = 0
        for i in range(1, len(nums)):
            if nums[pntSlow] != nums[i]:
                pntSlow += 1
                nums[pntSlow] = nums[i]
        return nums[0:pntSlow+1]





if __name__ == "__main__":
    solution = Solution
    a = solution.removeDuplicates(solution, [1,1,6,6])
    print(a)