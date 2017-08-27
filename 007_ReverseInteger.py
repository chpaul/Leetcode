class Solution(object):
    def reverse(self, x):
        """ 2147483647 ~ -2147483648
        :type x: int
        :rtype: int
        """
        revResult = 0
        if x >= 0:
            revResult = int(str(x)[::-1])
        else:
            revResult = -1 *  int (str(x)[:0:-1])
        if revResult > 2147483647 or revResult < -2147483648:
            return 0
        return revResult

if __name__ == "__main__":
    solution = Solution
    a = solution.reverse(solution, 0)
    print(a)