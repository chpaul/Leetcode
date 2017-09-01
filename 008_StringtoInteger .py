import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        str = re.findall('^[+\-]?\d+',str)
        try:
            result = int(''.join(str))
            if result > 2147483647:
                return 2147483647
            elif result <  -2147483648:
                return  -2147483648
            else:
                return  result
        except:
            return 0
if __name__ == "__main__":
    solution = Solution
    a = solution.myAtoi(solution, "+-2")
    print(a)