# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
3이라는 root가 있으니 최소 답이 1임. 길이가 1
그래서 return 1+max(left,right)
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node: 
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left,right)


        return dfs(root)