class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) ==0:
            return ''
        if len(strs) ==1:
            return strs[0]
        minLens = len(min(strs,key=len))
        if minLens ==0:
            return ''
        commLen = 0
        for i in range(0, minLens):
            isComm = True
            currChar = strs[0][i]
            for j in range(1,len((strs))):
                if strs[j][i] != currChar:
                    isComm = False
                    break
            if isComm:
                commLen+=1
            else:
                break
        return strs[0][0:commLen]


if __name__ == "__main__":
    solution = Solution
    array = ["",""]
    a = solution.longestCommonPrefix(solution, array)
    print(a)