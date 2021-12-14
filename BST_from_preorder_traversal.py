##Construct Binary Search Tree from Preorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self,node,val):
        if(node.val > val):
            if(node.left):
                node.left = self.insert(node.left,val)
            else:
                node.left = TreeNode(val)
        else:
            if(node.right):
                node.right = self.insert(node.right,val)
            else:
                node.right = TreeNode(val)
        return node
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            val = preorder[i]
            if(root.val > val):
                if(root.left):
                    self.insert(root.left,val)
                else:
                    root.left = TreeNode(val)
            elif(root.val < val):
                if(root.right):
                    self.insert(root.right,val)
                else:
                    root.right = TreeNode(val)
        return root
        
        
