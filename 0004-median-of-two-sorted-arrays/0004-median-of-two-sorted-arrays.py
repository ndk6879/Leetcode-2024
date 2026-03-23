class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # A를 더 짧은 배열로
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            mid1 = (l + r) // 2
            mid2 = half - mid1 - 2

            leftA = A[mid1] if mid1 >= 0 else float("-inf")
            rightA = A[mid1 + 1] if mid1 + 1 < len(A) else float("inf")
            leftB = B[mid2] if mid2 >= 0 else float("-inf")
            rightB = B[mid2 + 1] if mid2 + 1 < len(B) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2

            elif leftA > rightB:
                r = mid1 - 1
            else:
                l = mid1 + 1