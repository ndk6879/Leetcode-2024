class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        ans = []
        cur = []

        def dfs(i):
            if len(cur) >= len(digits):
                ans.append(''.join(cur.copy()))
                return

            elif i >= len(digits): return 

            for c in phone[digits[i]]:
                cur.append(c)
                dfs(i+1)

                cur.pop()
                dfs(i+1)

        dfs(0)
        return ans