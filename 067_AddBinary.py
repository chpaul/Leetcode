class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(b)> len(a):
            a,b= b,a
        if len(b) == '':
            return a

        revA = list(a[::-1])
        revB = list(b[::-1])
        carry = '0'
        for i in range(len(a)):
            if i<len(revB):
                combine = (revA[i] + revB[i] + carry).count('1')
            else:
                combine = (revA[i]  + carry).count('1')
            if combine ==3:
                revA[i]='1'
                carry = '1'
            elif combine ==2:
                revA[i] = '0'
                carry = '1'
            elif combine ==1:
                revA[i]='1'
                carry = '0'
            else:
                revA[i] = '0'
                carry = '0'
        if carry =='1':
            revA+='1'
        return ''.join(revA[::-1])

if __name__ == "__main__":
    solution = Solution()
    a = solution.addBinary('111','1')
    print(a)