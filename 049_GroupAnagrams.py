class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for i  in range(len(strs)):
            key  = ''.join(sorted(strs[i]))
            if key in result: result[key].append(i)
            else: result[key] =[i]
        res = []
        for key in result:
            category = []
            for i in result[key]:
                category.append(strs[i])
            res.append(category)
        return res

if __name__ == "__main__":
    solution = Solution()
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    a = solution.groupAnagrams(input)
    print(a)