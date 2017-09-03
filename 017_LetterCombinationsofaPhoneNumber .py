class Solution(object):
    def letterCombinations(self, digits):
        if digits=='':
            return []
        dictIntToNum = {"2":"abc","3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        SevenAndNineCount = digits.count("7")
        SevenAndNineCount += digits.count("9")
        TotalCount = 3 ** (len(digits) - SevenAndNineCount) * 4 ** SevenAndNineCount
        currentDivideIdx = TotalCount
        result = [''] * TotalCount
        for j in range(0,len(digits)):
            charStr = digits[j]
            if charStr == "7" or charStr == "9":
                currentDivideIdx /= 4
            else:
                currentDivideIdx /= 3
            for i in range(0,TotalCount):
                result[i] += dictIntToNum[charStr][int(i/currentDivideIdx)% len(dictIntToNum[charStr])]
        return  result



if __name__ == "__main__":
    solution = Solution
    a = solution.letterCombinations(solution, '772')
    print(a)