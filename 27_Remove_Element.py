# nums = [3, 2, 2, 3]
# count = 0
# tmp = 0
# for i in range(len(nums)):
#     if nums[i] != 3:
#         count += 1
#     else:
#         tmp = nums.pop(i)
#         nums.append(tmp)

# print(help(list))


nums = [3, 2, 2, 3]
val = 3

while val in nums:
    nums.remove(val)

print(nums)