class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        # x가 등장한 인덱스들을 수집
        indices = [i for i, num in enumerate(nums) if num == x]
        # 각 쿼리에 대한 결과를 반환
        return [indices[query - 1] if query <= len(indices) else -1 for query in queries]
