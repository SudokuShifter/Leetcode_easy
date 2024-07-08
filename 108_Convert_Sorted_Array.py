from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        tree = TreeNode()
        tree.val = nums[mid]
        tree.left = self.sortedArrayToBST(nums[:mid])
        tree.right = self.sortedArrayToBST(nums[mid + 1:])

        return tree