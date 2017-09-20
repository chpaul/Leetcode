class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0: return []
        result = []
        candidates.sort()
        candidates = list(filter(lambda x: x <= target, candidates))
        self.dfs(candidates, target, 0, [], result)
        return result

    def dfs(self, candidates, target, index, path, result):
        if target == 0 and path not in result:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            if candidates[i] > target:  # here
                break
            self.dfs(candidates, target - candidates[i], i+1, path + [candidates[i]], result)

if __name__ == "__main__":
    solution = Solution()
    a = solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(a)