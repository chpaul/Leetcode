class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        result = [0]* (len(num1) + len(num2))
        for i,n1 in  enumerate( reversed(num1)):
            for  j,n2 in enumerate(reversed(num2)):
                sum = int(n1) * int(n2)
                result[i+j] += sum
                result[i+j+1] += int(result[i+j]/10)
                result[i+j] %= 10
        #Trim 0
        while len(result) > 0 and result[-1] ==0:result.pop()
        return ''.join(map(str,result[::-1])) if len(result)>0 else "0"


if __name__ == "__main__":
    solution = Solution()
    a = solution.multiply("0","0")
    print(a)