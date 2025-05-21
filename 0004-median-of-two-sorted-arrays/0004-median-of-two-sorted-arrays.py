class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2

        if len(A) > len(B):
            A,B = B, A

        l, r = 0, len(A) - 1
        half = (len(A) + len(B)) // 2
# [0,0,0.     ,0,0,0,0]
# [0,0,    0,0]

        while True:
            i = (l + r) // 2 #A
            j = half - i - 2 #B

            leftA = A[i] if i >=0 else float("-inf")
            rightA = A[i+1] if i+1 < len(A) else float("infinity")
            leftB = B[j] if j >= 0 else float("-inf")
            rightB = B[j+1] if j+1 < len(B) else float("infinity")

            if leftA <= rightB and rightA >= leftB:

                if (len(A) + len(B)) % 2 == 0:
                    return (min(rightA,rightB) + max(leftA,leftB)) / 2

                else:
                    return min(rightA,rightB)

            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1

        