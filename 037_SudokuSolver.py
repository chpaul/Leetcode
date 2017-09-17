class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # smallestBoard = list(map(lambda x: x.count('.'),board))
        # smallestIdx = smallestBoard.index(min(smallestBoard))
        # posX = int(smallestIdx /3) * 3
        # posY = int(smallestIdx %3) * 3
        self.board =board
        self.dfs()
    def dfs(self):
        if sum(map(lambda x: x.count('.'), self.board)) == 0:
            return True
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    block = ''
                    for x in range(3):
                        for y in range(3):
                            block = block + self.board[int(i / 3) * 3 + x][int(j / 3) * 3 + y]
                    for char in range(1,10,1):
                        if (str(char) not in block) and (str(char) not in self.board[i]) and (str(char) not in ''.join(map(lambda x: x[j],self.board))):
                            self.board[i] = str(self.board[i][0:j]) + str(char) + str(self.board[i][j+1:10])
                            if self.isValidSudoku(self.board) is True:
                                if(self.dfs()):return True
                                else:
                                    self.board[i] = str(self.board[i][0:j]) + '.' + str(self.board[i][j+1:10])
                    return False
    # def dfs(self, board, posX, posY):
    #     block = ''
    #     for x in range(3):
    #         for y in range(3):
    #             block = block + board[int(posX / 3) * 3 + x][int(posY / 3) * 3 + y]
    #     for i in range(3):
    #         for j in range(3):
    #             if board[posX+i][posY+j] == '.':
    #                 for char in range(1,10,1):
    #                     if str(char) not in block:
    #                         newboard = board[:]
    #                         newboard[posX+i] = newboard[posX+i][0:posY+j] + str(char) + newboard[posX+i][posY+j+1:10]
    #                         if self.isValidSudoku(newboard) is True:
    #                             board[posX+i]= board[posX + i][0:posY + j] + str(char) + board[posX + i][posY + j+1:10]
    #                             smallestBoard = list(map(lambda x: x.count('.'), board))
    #                             smallestIdx = smallestBoard.index(min(smallestBoard))
    #                             posX = int(smallestIdx / 3) * 3
    #                             posY = int(smallestIdx % 3) * 3
    #                             self.dfs(board, posX, posY)



    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if  board[i].count(num) >1:
                        return False
                    col = ''.join(map(lambda x: x[j],board))
                    if  col.count(num) >1:
                        return False
                    block =''
                    for x in range(3):
                        for y in range(3):
                            block = block + board[int(i/3)*3 + x][int(j/3)*3+y]
                    if block.count(num) > 1:
                        return False
        return True

if __name__ == "__main__":
    solution = Solution()
    board = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
    a = solution.solveSudoku(board)
    print(a)