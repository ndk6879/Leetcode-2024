class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        - 1. if open == close == n: add to ans
        - 2. if open < n: +1 open
        - 3. if close < open: +1 close
        '''

        ans = []
        stack = []
        
        def dfs(openP, closeP):
            if openP == closeP == n:
                cur = "".join(stack)
                ans.append(cur)
                return

            if openP < n:
                stack.append('(')
                dfs(openP + 1 , closeP)
                stack.pop()

            if closeP < openP:
                stack.append(')')
                dfs(openP , closeP + 1)
                stack.pop()


        dfs(0,0)
        return ans

        