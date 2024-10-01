# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        1. if p < value < q: it's root
        2. elif value > p,q: then root = root.left
        3. elif value < p,q: then root = root.right
        '''
        if not root: return 0
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val: return root
        elif p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left,p,q)

        elif p.val >= root.val and q.val >= root.val: 
            return self.lowestCommonAncestor(root.right,p,q)

            
