class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  # 빈 입력 예외 처리
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        cur = []  # 전역 변수로 사용

        def dfs(index):
            if index == len(digits):  # 조합 완성되면 추가
                res.append(cur.copy())  # 복사 후 추가
                return

            for char in phone[digits[index]]:  # 해당 숫자의 문자들 탐색
                cur.append(char)  # 문자 추가
                dfs(index + 1)  # 다음 숫자로 이동
                cur.pop()  # 백트래킹 (이전 상태로 되돌리기)

        dfs(0)
        return ["".join(c) for c in res]