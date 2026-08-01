class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        k = 0
        for a in range(0, m+n):
            if j < m:
                if k < n:
                    if nums1[a] <= nums2[k]:
                        j += 1
                    else:
                        for b in range(m+n-1, a, -1):
                            nums1[b] = nums1[b-1]
                        nums1[a] = nums2[k]
                        k += 1
            else:
                nums1[a] = nums2[k]
                k += 1


        """
        Do not return anything, modify nums1 in-place instead.
        """
        
