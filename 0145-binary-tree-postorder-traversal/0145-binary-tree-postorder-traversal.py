# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #post order = left - right - root
        ans = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)
            return
        
        dfs(root)

        return ans
        