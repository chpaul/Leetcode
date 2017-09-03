class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m >n:
            nums1,nums2,m,n = nums2, nums1, n , m
        if n == 0:
            raise IndexError
        imin, imax= 0, m
        if (m+n)%2==1:
            helf_len = int((m+n+1) / 2)
        else:
            helf_len = int((m + n)  / 2)
        while imin<=imax:
            i = int( (imin + imax) / 2)
            j = int (helf_len - i)
            if 0 < i and  nums2[j] < nums1[i-1] :
                imax = i - 1
            elif i < m and nums1[i]< nums2[j-1] : # i too small increase i
                imin = i + 1
            else:  #(i==m or j==0 or nums1[i] >nums2[j-1] ) and (i==0 or j==n or nums1[i-1]<nums2[j] )
                if i ==0:
                    LeftMax = nums2[j-1]
                elif j ==0:
                    LeftMax = nums1[i-1]
                else:
                    LeftMax = max(nums1[i-1],nums2[j-1])
                if (n + m) %2 ==1:  # Odd case
                    return LeftMax

                if i ==m:
                    RightMin = nums2[j]
                elif j ==n:
                    RightMin = nums1[i]
                else:
                    RightMin = min(nums1[i],nums2[j])
                return (LeftMax + RightMin) / 2.0

if __name__ == "__main__":
    solution = Solution
    listA = [1,6,9,10]
    listB = [4]
    a = solution.findMedianSortedArrays(solution, listA,listB)
    print(a)