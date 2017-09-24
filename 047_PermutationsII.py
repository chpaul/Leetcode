class Solution(object):
    def permuteUnique(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    if perm[:i] + [n] + perm[i:] not in new_perms:
                        new_perms.append(perm[:i] + [n] + perm[i:])  ###insert n

            perms = new_perms
        return perms

if __name__ == "__main__":
    solution = Solution()
    a = solution.permuteUnique([1,1,3])
    print(a)