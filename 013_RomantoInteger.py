class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        dictRomToInt = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(0,len(s)-1):
            if dictRomToInt[s[i]] >= dictRomToInt[s[i+1]]:
                sum += dictRomToInt[s[i]]
            else:
                sum -= dictRomToInt[s[i]]
        sum+=dictRomToInt[s[len(s)-1]]
        return sum
if __name__ == "__main__":
    solution = Solution
    a = solution.romanToInt(solution, 'MMMCMXCIX')
    print(a)