class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('(') != s.count(')') or s.count('{') != s.count('}') or s.count('[') != s.count(']'):
            return False
        stk = []
        for i in range(0,len(s)):
            if s[i] == '(' or s[i] =='[' or s[i] == '{':
                stk.append(s[i])
            elif s[i] == ')':
                if stk[len(stk)-1] != '(': return False
                else: stk.pop()
            elif s[i] ==']' :
                if stk[len(stk)-1] != '[': return False
                else: stk.pop()
            elif s[i] == '}':
                if stk[len(stk)-1] != '{': return False
                else: stk.pop()
        if len(stk)!=0: return False
        return True

if __name__ == "__main__":
    solution = Solution
    a = solution.isValid(solution, "()[]{}")
    print(a)