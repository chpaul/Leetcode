class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) ==0:
            return []
        result = []

        idx,idy,  xlim, ylim = 0, 0, len(matrix),len(matrix[0])
        total = xlim * ylim
        seen = [[False] * ylim for _ in matrix]
        direction = 0  #0: row +0, col +1;  1:row +1, col  +0; 2: row+0, col -1; 3: row -1, col +0
        for i in range(total):
            result.append(matrix[idx][idy])
            seen[idx][idy] = True
            if direction ==0:
                idy+=1
                if idy == ylim or seen[idx][idy] == True : #turn
                    idx +=1
                    idy -=1
                    direction =1
            elif direction ==1:
                idx+=1
                if  idx == xlim or seen[idx][idy] == True : #turn
                    idx -=1
                    idy -=1
                    direction =2
            elif direction == 2:
                idy -= 1
                if idy == -1 or seen[idx][idy] == True:  # turn
                    idx -=1
                    idy += 1
                    direction = 3
            elif direction == 3:
                idx -= 1
                if idx == -1 or seen[idx][idy] == True :  # turn
                    idx += 1
                    idy += 1
                    direction = 0
        return result

if __name__ == "__main__":
    solution = Solution()
    maxtrix = [[ 1, 2, 3 ]]
    a = solution.spiralOrder(maxtrix)
    print(a)