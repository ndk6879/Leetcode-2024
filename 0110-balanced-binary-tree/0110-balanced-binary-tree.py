# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Diameter of Binary Tree를 DFS로 풀줄알면 개쉬움.
DFS의 1. base case와 2. recursive case를 고려
그리고 balanced인지 확인
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True

        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1: 
                self.balanced = False

            return 1 + max(left,right)

        dfs(root)

        return self.balanced