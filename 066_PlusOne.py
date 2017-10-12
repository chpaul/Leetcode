class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []
        for i in range(len(digits)-1,-1,-1):
            if digits[i] <9:
                digits[i]+=1
                return  digits
            else:
                digits[i] = 0


        digits.insert(0,1)
        return  digits






if __name__ == "__main__":
    solution = Solution()
    a = solution.plusOne([])
    print(a)