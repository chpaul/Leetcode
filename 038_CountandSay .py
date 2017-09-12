class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0 : return '0';
        if n == 1 : return '1';
        result = '1'
        for i in range(1,n):
            prv = ''
            newresult = ''
            count = 0
            for j in range(0,len(result)):
                if result[j] != prv:
                    if prv !='':
                        newresult +=  str(count)+prv
                    prv = result[j]
                    count = 1
                else: count+=1
            result = newresult + str(count)+ prv
        return  result

if __name__ == "__main__":
    solution = Solution
    for i in range(0,10):
        a = solution.countAndSay(solution, i)
        print(a)