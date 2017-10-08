class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n<0 or n ==2 or n==3:
            return []
        if n==1:
            return [["Q"]]

        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS([], [], [])
        return len(result)



if __name__ == "__main__":
    solution = Solution()
    a = solution.totalNQueens(4)
    print(a)