class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        plant =[[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            plant[0][i] =1
        for i in range(n):
            plant[i][0] =1
        for i in range(1,n):
            for j in range(1,m):
                plant[i][j] = plant[i-1][j] +  plant[i][j-1]
        return plant[n-1][m-1]

if __name__ == "__main__":
    solution = Solution()
    a = solution.uniquePaths(3,7)
    print(a)