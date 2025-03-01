class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        A, B = nums1, nums2
        
        if len(A) > len(B):
            A, B = B, A

        start, end = 0, len(A) - 1    
        while True:
            
            mid1 = (start + end ) // 2
            mid2 = ((len(A) + len(B)) // 2) - mid1 - 2

            Aleft = A[mid1] if mid1 >= 0 else float("-infinity")
            Aright = A[mid1+1] if mid1+1 < len(A) else float("infinity")
            Bleft = B[mid2] if mid2 >= 0 else float("-infinity")
            Bright = B[mid2+1] if mid2+1 < len(B) else float("infinity")

            if (Aleft <= Bright and Bleft <= Aright):
                if (len(A) + len(B)) % 2 == 0:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2

                else:
                    return min(Aright, Bright)

            elif Aleft > Bright:
                end = mid1 - 1

            else:
                start = mid1 + 1