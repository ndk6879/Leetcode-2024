# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, val):
            if not node: return 0
            
            if node.val >= val:
                self.ans += 1

            val = max(node.val , val) 
            
            left = dfs(node.left, val)
            right = dfs(node.right, val)
            return 1 + max(left,right)

        dfs(root,root.val)


        return self.ans