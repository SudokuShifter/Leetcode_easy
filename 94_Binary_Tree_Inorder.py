from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_res = []
        self.inorder(root, list_res)
        return list_res

    def inorder(self, node, some_list: List[int]):
        if node:
            self.inorder(node.left, some_list)
            some_list.append(node.val)
            self.inorder(node.right, some_list)