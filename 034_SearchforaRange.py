class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x =  [i for i in map(lambda x: x==target,nums)]
        idx = [i[0] for i in filter(lambda x: x[1] == True,enumerate(x))]
        if len(idx) ==0: return [-1,-1]
        elif len(idx)==1: return [idx[0],idx[0]]
        else:return [idx[0],idx[len(idx)-1]]


if __name__ == "__main__":
    solution = Solution
    a = solution.searchRange(solution, [3,3,3],3)
    print(a)