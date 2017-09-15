class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if self.hasDuplicate(board[i]):
                    return False
                col = ''.join(map(lambda x: x[j], board))
                if self.hasDuplicate(col):
                    return False
                block = ''
                for x in range(3):
                    for y in range(3):
                        block = block + board[int(i / 3) * 3 + x][int(j / 3) * 3 + y]
                    if self.hasDuplicate(block):
                        return False
        return True

    def hasDuplicate(self,Str):
        newStr = str(Str).replace('.', '')
        for i in range(len(newStr)):
            if newStr.count(newStr[i]) >1:
                return True
        return False

# class Solution(object):
#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         for i in range(9):
#             for j in range(9):
#                 num = board[i][j]
#                 if num != '.':
#                     if  board[i].count(num) >1:
#                         return False
#                     col = ''.join(map(lambda x: x[j],board))
#                     if  col.count(num) >1:
#                         return False
#                     block =''
#                     for x in range(3):
#                         for y in range(3):
#                             block = block + board[int(i/3)*3 + x][int(j/3)*3+y]
#                     if block.count(num) > 1:
#                         return False
#         return True


if __name__ == "__main__":
    solution = Solution()
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    #board = [".........",".........",".9......1","8........",".99357...",".......4.","...8.....",".1....4.9","...5.4..."]
    board = ["7...4....","...865...",".1.2.....",".....9...","....5.5..",".........","......2..",".........","........."]
    a = solution.isValidSudoku(board)
    print(a)