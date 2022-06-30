import math
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        gap = math.ceil((m+n)/2)
        while gap>0:
            i = 0
            j = gap
            while j < (n+m) :
                if j < m and nums1[i] > nums1[j]:
                    nums1[i],nums1[j]=nums1[j],nums1[i]
                elif j >= m and i < m and nums1[i] > nums2[j-m]:
                    nums1[i],nums2[j-m] = nums2[j-m],nums1[i]
                elif j >= m and i >= m and nums2[i-m] > nums2[j-m]:
                    nums2[i-m],nums2[j-m] = nums2[j-m],nums2[i-m]
                i+=1
                j+=1
            if gap ==1:
                gap = 0
            else:
                gap = math.ceil(gap/2)
            
        
        
        x = 0
        while x < n:
            nums1[m]=nums2[x]
            m+=1
            x+=1
            
            
        