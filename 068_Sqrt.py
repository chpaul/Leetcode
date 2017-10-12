class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right= 1, x
        while(True):
            mid = (right+left)//2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid + 1




if __name__ == "__main__":
    solution = Solution()
    a = solution.mySqrt(4)
    # 2147395600          46340
    # 2147483647          46340
    print(a)