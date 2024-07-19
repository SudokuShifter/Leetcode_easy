from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        list_res = []
        sup_list = []

        while nums:
            if not sup_list or sup_list[-1] + 1 == nums[0]:
                sup_list.append(nums.pop(0))
            else:
                if len(sup_list) > 1:
                    list_res.append(f'{sup_list[0]}->{sup_list[-1]}')
                else:
                    list_res.append(f'{sup_list[0]}')
                sup_list = []

        if sup_list:
            if len(sup_list) > 1:
                list_res.append(f'{sup_list[0]}->{sup_list[-1]}')
            else:
                list_res.append(f'{sup_list[0]}')

        return list_res
