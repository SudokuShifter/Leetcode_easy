from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1).intersection(set(nums2)))
        return list(set(nums1) & set(nums2))

