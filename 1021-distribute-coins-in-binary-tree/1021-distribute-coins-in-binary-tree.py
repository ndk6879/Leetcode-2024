class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # 이동 횟수 누적
            self.ans += abs(left) + abs(right)

            # 현재 노드의 잔여 동전
            return node.val + left + right - 1

        dfs(root)
        return self.ans
