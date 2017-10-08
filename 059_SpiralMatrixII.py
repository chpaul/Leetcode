class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==1:
            return [[1]]
        result = []
        for i in range(n):
            result.append([0] * n)

        idx,idy = 0, 0
        total = n * n

        direction = 0  #0: row +0, col +1;  1:row +1, col  +0; 2: row+0, col -1; 3: row -1, col +0
        num = 1
        for i in range(total):
            result[idx][idy] = num
            num+=1
            if direction ==0:
                idy+=1
                if idy == n or result[idx][idy] != 0 : #turn
                    idx +=1
                    idy -=1
                    direction =1
            elif direction ==1:
                idx+=1
                if  idx == n or result[idx][idy] != 0 : #turn
                    idx -=1
                    idy -=1
                    direction =2
            elif direction == 2:
                idy -= 1
                if idy == -1 or result[idx][idy] != 0:  # turn
                    idx -=1
                    idy += 1
                    direction = 3
            elif direction == 3:
                idx -= 1
                if idx == -1 or result[idx][idy] != 0 :  # turn
                    idx += 1
                    idy += 1
                    direction = 0
        return result

if __name__ == "__main__":
    solution = Solution()
    a = solution.generateMatrix(3)
    print(a)