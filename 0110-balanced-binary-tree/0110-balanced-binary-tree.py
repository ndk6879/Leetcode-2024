# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True

        def dfs(root):
            if not root: return 0

            left = dfs(root.left)
            right = dfs(root.right)
            if abs(right - left) > 1:
                self.balance = False

            return 1 + max(left,right)

        dfs(root)
        return self.balance