class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left<right:
            mid = int((left + right) / 2)
            if (target < nums[0]) ^ (nums[0] > nums[mid]) ^  (target > nums[mid]):
                left = mid+1
            else: right = mid
        return left if target in nums[left:left+1] else -1



if __name__ == "__main__":
    solution = Solution
    a = solution.search(solution, [5,1,3],1)
    print(a)