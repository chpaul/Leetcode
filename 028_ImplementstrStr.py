class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack: return -1
        if needle == haystack: return 0;
        haystackLen = len(haystack)
        needleLen = len(needle)
        if needleLen > haystackLen: return -1
        if needle == None or needleLen == 0 : return 0

        for i in range(0, haystackLen - needleLen+1):
            found = None
            if haystack[i] == needle[0]:
                for j in range(1, needleLen):
                    if haystack[i+j] != needle[j]:
                        found = False
                if found != False:
                    return i
        return -1


if __name__ == "__main__":
    solution = Solution
    a = solution.strStr(solution, 'mississippi', 'issip')
    print(a)