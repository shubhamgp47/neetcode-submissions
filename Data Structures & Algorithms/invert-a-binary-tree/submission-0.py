# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        def rev(root):
            if not root:
                return
            #swap childern
            temp=root.left
            root.left=root.right
            root.right=temp
            # recursion
            rev(root.left)
            rev(root.right)
        rev(root)
        return root