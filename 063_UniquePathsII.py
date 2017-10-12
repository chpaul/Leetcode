class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] ==1:
            return 0

        lenX = len(obstacleGrid)
        lenY = len(obstacleGrid[0])
        if obstacleGrid[0][0] ==0 and lenX==1 and lenY==1:
            return 1
        for i in range(lenX):
            obstacleGrid[i][0] = 1 if obstacleGrid[i][0]!=1 else 0
            if i>0 and obstacleGrid[i-1][0]==0:
                obstacleGrid[i][0] =0
        for i in range(1,lenY):
            obstacleGrid[0][i] = 1 if obstacleGrid[0][i] !=1 else 0
            if i>0 and obstacleGrid[0][i-1]==0:
                obstacleGrid[0][i] =0

        for i in range(1,lenX):
            for j in range(1,lenY):
                if obstacleGrid[i][j] ==1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j] +obstacleGrid[i][j-1]

        return obstacleGrid[lenX-1][lenY-1]

if __name__ == "__main__":
    solution = Solution()
    # A = [[0,0,0],[0,1,0],[0,0,0]]
    A = [[0,0]]
    a = solution.uniquePathsWithObstacles(A)
    print(a)