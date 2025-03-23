# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0


        def dfs(root, rootVal):
            if not root: return 0

            if root.val >= rootVal:
                self.ans += 1

            if root.left:
                dfs(root.left, max(rootVal, root.left.val))
            if root.right:
                dfs(root.right, max(rootVal, root.right.val))
            

        dfs(root,root.val)

        return self.ans
        