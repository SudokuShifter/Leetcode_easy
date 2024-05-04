nums = [1, 2, 5, 7, 8]
target = 4


def searchInsert(nums: list[int], target: int) -> int:
    if target > nums[-1]:
        return len(nums)
    else:
        i = 0
        while target > nums[i] and i < len(nums):
            i += 1
        return i
