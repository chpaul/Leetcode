class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <=1: return 0
        allWater = 0
        leftIdx, rightIdx = 0, len(height) -1
        leftMax, rightMax = 0,0
        while leftIdx < rightIdx:
            if height[leftIdx] < height[rightIdx]:
                if height[leftIdx] >leftMax:leftMax = height[leftIdx]
                else:allWater+= leftMax - height[leftIdx]
                leftIdx+=1
            else:
                if height[rightIdx] >rightMax: rightMax = height[rightIdx]
                else:allWater+= rightMax -height[rightIdx]
                rightIdx-=1
        return allWater
if __name__ == "__main__":
    solution = Solution()
    a = solution.trap([4,2,0,3,2,5])  # 9
    a = solution.trap([5,2,1,2,1,5]) #14
    a = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])

    print(a)