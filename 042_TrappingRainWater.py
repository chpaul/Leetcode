class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <=1: return 0
        allWater = 0
        leftIdx, rightIdx = 0,0
        leftMax, rightMax = 0,0
        for i in range(1,len(height)-1):
            if i >=rightIdx:
                rightIdx = i+1
                while rightIdx< len(height)-1:
                    rightIdx+=1
                    if rightMax <= height[rightIdx]:
                        rightMax=height[rightIdx]
            leftIdx = i -1 if i-1>0 else 0
            while leftIdx >= 0:
                if leftMax<=height[leftIdx]:
                    leftMax = height[leftIdx]
                leftIdx -= 1

            allWater += min(height[leftIdx],height[rightIdx])-height[i] if  min(height[leftIdx],height[rightIdx])-height[i]  >0 else 0
        return allWater
if __name__ == "__main__":
    solution = Solution()
    a = solution.trap([5,2,1,2,1,5]) #14
    a = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])

    print(a)