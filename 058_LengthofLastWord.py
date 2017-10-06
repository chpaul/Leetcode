class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0:
            return 0

        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                length += 1
            elif length != 0:
                break
        return length

if __name__ == "__main__":
    solution = Solution()
    a = solution.lengthOfLastWord('helloworld')
    print(a)