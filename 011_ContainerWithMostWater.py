class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right = 0,len(height)-1
        maxArea = 0
        while(left<right):
            minHeight = min(height[left],height[right])
            maxArea = max(maxArea, (right-left) * minHeight)
            while left<right and height[left] <= minHeight:
                left+=1
            while left<right and height[right] <= minHeight:
                right-=1
        return maxArea

if __name__ == "__main__":
    solution = Solution
    a = solution.maxArea(solution, (1,2,3,4,5))
    print(a)