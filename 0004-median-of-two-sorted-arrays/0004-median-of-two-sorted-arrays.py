class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A,B = nums1, nums2
        if len(A) > len(B):
            A,B = B,A

        
        start, end = 0, len(A) - 1

        while True:
            mid1 = (start + end) // 2
            mid2 = (len(A) + len(B)) // 2 - mid1 - 2

            leftA = A[mid1] if mid1 >= 0 else float("-infinity")
            rightA = A[mid1+1] if mid1+1 < len(A) else float("infinity") 
            leftB = B[mid2] if mid2 >= 0 else float("-infinity")
            rightB = B[mid2+1] if mid2+1 < len(B) else float("infinity")

            if leftA <= rightB and leftB <= rightA:
                if (len(A) + len(B)) % 2 == 0:
                    return (max(leftA,leftB) + min(rightA,rightB)) / 2

                else:
                    return min(rightA,rightB)

            elif leftA > rightB:
                end = mid1 -1
            
            else:
                start = mid1 + 1