class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0 :return ['']
        if n == 1 :return ['()']
        results = []
        processing = []
        processing.append('(')
        while len(processing)!=0:
            tmp = processing.pop(0)
            if tmp.count('(') <n:
                left = tmp + '('
                if left.count('(') >= left.count(')'): #vaild
                    if left.count('(') == n and left.count(')') ==n: results.append(left)
                    else:processing.append(left)
            if tmp.count(')') < n:
                right = tmp + ')'
                if right.count('(') >= right.count(')'): #vaild
                    if right.count('(') == n and right.count(')') ==n: results.append(right)
                    else:processing.append(right)
        return results


if __name__ == "__main__":
    solution = Solution
    a = solution.generateParenthesis(solution, 3)
    print(a)