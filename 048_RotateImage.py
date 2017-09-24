class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix = list(reversed(matrix))
        for i in range(len(matrix)):
            for j in range (i,len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)

if __name__ == "__main__":
    solution = Solution()
    a = solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    a = solution.rotate([[1,2,3],[4,5,6],[7,8,9]])  # [[7,4,1],[8,5,2],[9,6,3]]
    print(a)