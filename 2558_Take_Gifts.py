import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        while i < k:
            gifts = sorted(gifts)
            sqrt = math.floor(math.sqrt(gifts[-1]))
            gifts[-1] = sqrt
            i +=1
        return int(sum(gifts))