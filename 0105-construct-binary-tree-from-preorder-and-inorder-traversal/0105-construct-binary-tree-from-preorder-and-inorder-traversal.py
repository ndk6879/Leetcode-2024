# class Node:
#     def __init__(self,val = None,left = None,right = None):
#         self.val = None
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = root - left - right
        # inorder = left - root - right
        if not preorder or not inorder:
            return None


        root = TreeNode()
        root.val = preorder[0]
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root 