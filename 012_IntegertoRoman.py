class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0 or num >3999:
            return ''
        strResult = ''
        dictIntToRam = ["I","II","III","IV","V","VI","VII","VIII","IX",
                        "X", "XX","XXX","XL","L","LX","LXX","LXXX","XC",
                        "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
                        "M", "MM", "MMM"]
        strResult =  '' if int(num / 1000) == 0 else dictIntToRam[ int(num / 1000)+ 26]
        strResult += '' if int(num / 100)%10 == 0 else dictIntToRam[int(num / 100)%10 + 17]
        strResult += '' if int(num / 10)%10 == 0 else dictIntToRam[int(num / 10)%10 +8]
        strResult += '' if int(num % 10) == 0 else dictIntToRam[int(num %10) -1]
        return strResult



if __name__ == "__main__":
    solution = Solution
    a = solution.intToRoman(solution, 3999)
    print(a)