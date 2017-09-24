class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if '?' not in p and '*' not in p and s != p: return False
        if s == p: return True
        pLen = len(p)
        sIdx, pIdx, starIdx, matchIdx = 0, 0, -1, 0
        while sIdx <len (s) :
            if pIdx < pLen and (s[sIdx] == p[pIdx] or p[pIdx]=='?'):
                sIdx+=1
                pIdx+=1
            elif pIdx<pLen and p[pIdx] == '*':
                starIdx = pIdx
                pIdx += 1
                matchIdx = sIdx
            elif starIdx!=-1:
                pIdx = starIdx+1
                matchIdx+=1
                sIdx = matchIdx
            else: return False
        while pIdx<pLen and p[pIdx]=='*': pIdx+=1
        return pIdx == pLen

if __name__ == "__main__":
    solution = Solution()
    a = solution.isMatch('abaaaa','a*aa')
    print(a)