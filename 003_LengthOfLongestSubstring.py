class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        startIdx = 0
        usedChars = []
        targetStr = ""
        for j in range(0, len(s)):
            del usedChars[:]
            curStr = ""
            for i in range(j,len(s)):
                nextChar = s[i]
                if nextChar not in usedChars:
                    usedChars.append(nextChar)
                    curStr+= nextChar
                else:
                    startIdx += i-1
                    break
                if len(curStr) > len(targetStr):
                    targetStr = curStr
        return len(targetStr)

if __name__ == "__main__":
    solution = Solution
    a = solution.lengthOfLongestSubstring(solution, "aab")
    a = solution.lengthOfLongestSubstring(solution, "dvdf")
    print(a)