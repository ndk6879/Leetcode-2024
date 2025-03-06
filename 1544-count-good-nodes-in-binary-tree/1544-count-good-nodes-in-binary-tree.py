# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, val):
            nonlocal ans
            if not node:
                return

            if node.val >= val:
                ans += 1

            if node.val >= val:
                val = node.val

            dfs(node.left, val)
            dfs(node.right, val)


        dfs(root,root.val)
        
        return ans