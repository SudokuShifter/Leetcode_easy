class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = int(str(num)[::-1])
        return int(str(n)[::-1]) == num