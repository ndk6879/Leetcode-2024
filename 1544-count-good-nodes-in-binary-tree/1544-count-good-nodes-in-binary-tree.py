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
            #base case
            if not node: return

            if node.val >= val:
                self.ans += 1

            #recursive case
            greatestValue = max(node.val, val)
            dfs(node.left, greatestValue) 
            dfs(node.right, greatestValue)
            return

        dfs(root, root.val)
        return self.ans
        