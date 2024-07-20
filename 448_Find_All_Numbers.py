from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = list(range(1, n+1))
        for i in nums:
            a[i-1] = None
        return [i for i in a if i]
