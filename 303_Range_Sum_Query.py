from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0]
        for i in self.nums:
            self.sums.append(self.sums[-1] + i)
        self.sums = self.sums[1:]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        else:
            return self.sums[right] - self.sums[left - 1]



