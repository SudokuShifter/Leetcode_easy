from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        res = []
        for n in nums2:
            if n in counts and counts[n] > 0:
                res.append(n)
                counts[n] -= 1
        return res
