from math import floor
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [x for x in range(1,n+1)]
        premutationCount = [1] * (n +1)
        for i in range(1,n+1):
            premutationCount[i] = premutationCount[i-1] * i

        if k> premutationCount[n]: # index out of range
            return ''
        result = ''
        k-=1
        for i in range(1,n+1):
            idx = floor( k / premutationCount[n-i])
            result += str(nums[idx])
            nums.pop(idx)
            k -= (idx * premutationCount[n-i])
        return result



if __name__ == "__main__":
    solution = Solution()
    a = solution.getPermutation(3,2)
    print(a)