from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_miracle(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and is_miracle(left.left, right.right)) and is_miracle(left.right, right.left)
        return is_miracle(root.left, root.right)
