class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        - Use A,B where A is smaller
        - Find med1, med2 where they partition left part of each array
        - find leftA, rightA, leftB, rightB
        - if leftA <= rightB and leftB <= rightA: -> can find answer
        - elif leftA > rightB: right = mid1 - 1
        - else: left = mid + !
        '''

        A,B = nums1, nums2

        if len(A) > len(B):
            A,B = B, A

        l,r = 0, len(A) - 1

        while True:
            med1 = (l + r) // 2
            med2 = (len(A) + len(B)) // 2 - med1 - 2

            leftA = A[med1] if med1 >= 0 else float("-inf")
            rightA = A[med1+1] if med1+1 < len(A) else float("inf")
            leftB = B[med2] if med2 >= 0 else float("-inf")
            rightB = B[med2+1] if med2+1 < len(B) else float("inf")
            
            if leftA <= rightB and leftB <= rightA:
                #odd
                if (len(A) + len(B)) % 2 == 1:
                    return min(rightA,rightB)

                #odd
                else:
                    return (max(leftA,leftB) + min(rightA,rightB)) / 2
            
            elif leftA > rightB:
                r = med1 - 1

            else:
                l = med1 + 1