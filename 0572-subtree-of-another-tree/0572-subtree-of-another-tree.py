# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):

            if not p and not q: 
                return True
                
            if p and not q: 
                print(2)
                return False
            
            if not p and q: 
                print(1)
                return False


            if p.val != q.val: 
                print(3)
                return False

            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        if not subRoot: return True
        if not root: return False
        if  isSameTree(root, subRoot): return True
        return isSameTree(root.left, subRoot) or isSameTree(root.right, subRoot)