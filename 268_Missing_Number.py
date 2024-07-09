from typing import List


def missingNumber(self, nums: List[int]) -> int:
    len_array = len(nums)
    check_sum = (len_array * (len_array + 1)) // 2

    return check_sum - sum(nums)