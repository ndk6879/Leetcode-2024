# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
이것도 DFS를 이용해 풀면됨.
base case와 recursive case때 어떻게 할지 생각하면서 풀면 쉽게 가능.
햇갈리면 이전에 543. Diameter of Binary Tree, 110. Balanced Binary Tree 같은 DFS문제 ㄱㄱ
'''

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
        