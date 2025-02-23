class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = []

        def dfs(openP,closedP):

            if openP == closedP == n:
                tmp = ''.join(cur)
                ans.append(tmp)
                return

            if openP < n:
                cur.append('(')
                dfs(openP+1,closedP)
                cur.pop()

            if closedP < openP:
                cur.append(')')
                dfs(openP, closedP + 1)
                cur.pop()




        dfs(0, 0)
        return ans