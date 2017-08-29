class Solution(object):
    def longestPalindrome(self, s):
        if len(s)< 2:
            return s
        maxStr = ""
        for i in range(len(s)):
            j = i
            k = i
            while j>=0 and k<len(s) and (s[j:i+1] == s[i:k+1][::-1]):
                j -=1
                k +=1

            j = j+1 if j >=0 else 0
            k = k-1 if k <= len(s) else len(s)-1
            if len(maxStr) < len(s[j:k+1]):
                maxStr =s[j:k+1]
            j =i
            k= i+1
            while j>=0 and k<len(s) and (s[j:i+1] == s[i+1:k+1][::-1]):
                j -=1
                k +=1
            j = j + 1 if j >= 0 else 0
            k = k - 1 if k <= len(s) else len(s) - 1
            if len(maxStr) < len(s[j:k+1]):
                maxStr = s[j:k + 1]
        return maxStr

if __name__ == "__main__":
    solution = Solution
    a = solution.longestPalindrome(solution, "ccc")
    print(a)