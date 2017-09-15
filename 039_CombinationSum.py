class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0: return []
        result = []
        candidates.sort()
        self.dfs(candidates,target,0,[], result)
        return result

    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:  # here
                break
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

if __name__ == "__main__":
    solution = Solution()
    a = solution.combinationSum([2,3,6,7], 7)
    print(a)