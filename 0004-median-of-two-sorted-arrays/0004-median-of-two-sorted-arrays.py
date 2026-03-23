class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # 항상 A를 더 짧은 배열로 만들어서 binary search 안정화
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2  # 왼쪽 파티션에 들어갈 총 개수

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2            # A에서 왼쪽 파티션의 마지막 index
            j = half - i - 2            # B에서 왼쪽 파티션의 마지막 index

            # 경계 처리 (배열 밖이면 -inf / inf로 처리)
            Aleft  = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft  = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            # 올바른 partition인지 체크
            # 왼쪽 최대 <= 오른쪽 최소가 되어야 함
            if Aleft <= Bright and Bleft <= Aright:
                
                # 홀수 개면 오른쪽 쪽의 첫 값이 median
                if total % 2:
                    return min(Aright, Bright)
                
                # 짝수 개면 왼쪽 최대 + 오른쪽 최소 / 2
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # A의 왼쪽 값이 너무 크면 → 왼쪽으로 이동
            elif Aleft > Bright:
                r = i - 1

            # B의 왼쪽 값이 너무 크면 → 오른쪽으로 이동
            else:
                l = i + 1