class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """


if __name__ == "__main__":
    solution = Solution()
    a = solution.findSubstring('barfoothefoobarman', ["foo", "bar"])
    print(a)