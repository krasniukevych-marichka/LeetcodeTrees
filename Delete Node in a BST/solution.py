# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            if not root.left and root.right:
                return root.right
            if root.left and not root.right:
                return root.left
            if root.left and root.right:
                min_node = root.right
                while min_node.left:
                    min_node = min_node.left
                root.val = min_node.val
                root.right = self.deleteNode(root.right, root.val)
        return root