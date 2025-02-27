from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsMap = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            crsMap[crs].append(preq)

        visit = [0] * numCourses  # 방문 상태 (0: 미방문, 1: 방문 중, 2: 방문 완료)
        ans = []

        def dfs(i):
            if visit[i] == 1:  # 탐색 중인 노드를 다시 방문 → 사이클 발생
                return False
            if visit[i] == 2:  # 이미 방문 완료된 노드 → 건너뜀
                return True

            visit[i] = 1  # 방문 중 표시
            for preq in crsMap[i]:
                if not dfs(preq): return False
            visit[i] = 2  # 방문 완료 후 추가

            ans.append(i)  # 후위 순회로 저장
            return True

        for i in range(numCourses):
            if not dfs(i):  # 사이클이 있으면 빈 배열 반환
                return []

        return ans  # 원래 순서대로 반환
