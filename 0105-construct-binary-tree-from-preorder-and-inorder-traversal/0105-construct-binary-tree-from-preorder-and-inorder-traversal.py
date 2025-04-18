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

        root = TreeNode(preorder[0])
        rootIndex = inorder.index(preorder[0]) #left subtree에 몇개의 노드가 있는지 알수있음
        root.left = self.buildTree(preorder[1:1+rootIndex], inorder[:rootIndex])
        root.right = self.buildTree(preorder[1+rootIndex:], inorder[1+rootIndex:])
        return root