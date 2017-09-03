class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if '.' not in p and '*' not in p :
            if s ==p : return True
            else: return False
        sLen = len(s)
        pLen = len(p)
        sIdx = 0
        pIdx = 0
        match = True
        while sIdx < sLen and pIdx <pLen:
            curChar = s[sIdx]
            if s[sIdx] == p[pIdx] or p[pIdx] == '.':
                sIdx ,pIdx = sIdx+1,pIdx+1
            elif pIdx < pLen -1 and p[pIdx+1] =='*':
                while s[sIdx] == p[pIdx]: sIdx+=1
                pIdx+=2
            elif p[pIdx] =='*' and (p[pIdx-1] == s[sIdx] or p[pIdx-1]=='.'):
                while sIdx<sLen and (s[sIdx] == p[pIdx-1] or p[pIdx-1]=='.'): sIdx += 1
                pIdx+=1
            else:
                match = False
                break
        if sIdx!=sLen : return  False
        if pIdx!=pLen :
            if sIdx!=sLen and p[pIdx] == s[pIdx]: return True
            else: return False

        return match


if __name__ == "__main__":
    solution = Solution
    a = solution.isMatch(solution, 'aaa', 'a*a')
    print("Correct" if a == True else "None Correct")
    a = solution.isMatch(solution, 'ab', '.*c')
    print("Correct" if a == False else "None Correct")
    a = solution.isMatch(solution, 'aa', 'a')
    print("Correct" if a == False else "None Correct")
    a = solution.isMatch(solution, 'aa', 'aa')
    print("Correct" if a == True else "None Correct")
    a = solution.isMatch(solution, 'aaa', 'aa')
    print("Correct" if a == False else "None Correct")
    a = solution.isMatch(solution, 'aa', 'a*')
    print("Correct" if a == True else "None Correct")
    a = solution.isMatch(solution, 'aa', '.*')
    print("Correct" if a == True else "None Correct")
    a = solution.isMatch(solution, 'ab', '.*')
    print("Correct" if a == True else "None Correct")
    a = solution.isMatch(solution, 'aab', 'c*a*b')
    print("Correct" if a == True else "None Correct")

