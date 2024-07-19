def isBadVersion(ver: int) -> bool:
    return ...


class Solution:
    def firstBadVersion(self, n: int) -> int:

        left = 0
        right = n
        while left < right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left    