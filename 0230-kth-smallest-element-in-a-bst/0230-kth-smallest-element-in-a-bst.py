# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        arr = []
        def helper(node):
            if not node: return 
            if node.left: helper(node.left)
            arr.append(node.val)

            if node.right: 
                helper(node.right)
            
        
        helper(root)
        print('arr:',arr)
        return arr[k-1]
        