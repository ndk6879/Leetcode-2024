class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_map = {}  # 대각선을 저장할 딕셔너리
        
        # 2차원 배열을 순회하며 대각선 인덱스(i + j)로 원소 저장
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j not in diagonal_map:
                    diagonal_map[i + j] = []
                diagonal_map[i + j].append(nums[i][j])
        
        result = []
        # 대각선 인덱스 순서대로 원소들을 결과 리스트에 추가
        for key in sorted(diagonal_map.keys()):
            # 대각선별로 저장된 원소들을 뒤집어서 추가
            result.extend(diagonal_map[key][::-1])
        
        return result
