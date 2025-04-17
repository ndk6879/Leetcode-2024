class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return 0

            l = max(0, dfs(node.left))   # 음수 경로는 버리기 위해 max(0, ...)
            r = max(0, dfs(node.right))

            self.ans = max(self.ans, node.val + l + r)

            return node.val + max(l, r)

        dfs(root)
        return self.ans
