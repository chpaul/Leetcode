class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_max_reach, current_max_reach = 0, 0
        i = 0
        while current_max_reach < len(nums) - 1:
            while i <= last_max_reach:
                current_max_reach = max(i + nums[i], current_max_reach)
                i += 1
            if last_max_reach == current_max_reach:
                return False
            last_max_reach = current_max_reach
        return True

if __name__ == "__main__":
    solution = Solution()
    a = solution.canJump([2,3,1,1,4])
    print(a)