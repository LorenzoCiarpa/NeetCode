class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L = nums1.copy()
        R = nums2.copy()

        i,j,k = 0, 0, 0

        while i < m and j < n:
            if L[i] < R [j]:
                nums1[k] = L[i]
                i += 1
            else:
                nums1[k] = R[j]
                j += 1

            k += 1
        
        while i < m:
            nums1[k] = L[i]
            i += 1
            k += 1
        
        while j < n:
            nums1[k] = R[j]
            j += 1
            k += 1
        