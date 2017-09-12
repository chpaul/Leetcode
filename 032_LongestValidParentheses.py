import re
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = s
        while len(re.findall('\(\**\)',result))>0:
            matched = re.findall('\(\**\)',result)[0]
            result =result.replace(matched, matched[1:-1]+'*')

        max,count = 0,0

        for i in range(len(result)):
            if result[i] == '*': count+=1;
            else:
                max = count if count>max else max
                count = 0
        max = count if count > max else max
        return max*2

if __name__ == "__main__":
    solution = Solution
    a = solution.longestValidParentheses(solution, '()(())')
    print(a)