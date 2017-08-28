class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        set = []
        ans = 0
        i= 0
        j = 0
        while i<n and j<n:
            if s[j] not in set:
                set.append(s[j])
                j+=1
                ans = j-i if j-i > ans else ans
            else:
                set.remove(s[i])
                i+=1
        return ans

if __name__ == "__main__":
    solution = Solution
    a = solution.lengthOfLongestSubstring(solution, "aab")
    a = solution.lengthOfLongestSubstring(solution, "dvdf")
    print(a)