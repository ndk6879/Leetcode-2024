# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #preorder = root - [left.subtree] - [right.subtree]
        #inorder = [left.subtree] - root - [right.subtree]

        if not preorder and not inorder: return 

        rootValue = preorder[0]
        root = TreeNode(rootValue)
        rootIndex = inorder.index(rootValue)
        root.left = self.buildTree (preorder[1:1+rootIndex] , inorder[:rootIndex] )
        root.right = self.buildTree (preorder[1+rootIndex:] , inorder[rootIndex+1:] )
        return root