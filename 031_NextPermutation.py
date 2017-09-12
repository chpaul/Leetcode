class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 0: return
        elif len(nums) == 1: return
        elif len(nums) == 2 or all(earlier >= later for earlier, later in zip(nums, nums[1:])):
            nums[0:] = list(reversed(nums))
            return
        else:
            leftIdx = len(nums)-2
            for i in range(len(nums)-2, -1 ,-1):
                if nums[i]>= nums[i+1]: leftIdx=i
                else:
                    leftIdx=i
                    break
            targetIdx = list(nums[leftIdx+1:]).index(min(list(filter(lambda x: x>nums[leftIdx],nums[leftIdx+1:])))) + leftIdx+1
            nums[leftIdx],nums[targetIdx] = nums[targetIdx], nums[leftIdx]
            nums[leftIdx+1:] = list(sorted(nums[leftIdx+1:]))

if __name__ == "__main__":
    solution = Solution
    a = [5,4,7,5,3,2]
    #a = [1,2,3]
    while True:
        solution.nextPermutation(solution, a)
        print(a)
