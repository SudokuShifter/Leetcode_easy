import math

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n <= 0 or n % 2:
            return False
        if math.log(n, 4).is_integer():
            return True
        return False