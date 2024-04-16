
nums = [1, 1, 2, 2, 3, 4, 4, 5, 6, 5, 6]

check_point = nums[0]
for i in range(1, len(nums)):
    check_point = check_point ^ nums[i]
    print(f'check_point:= {check_point}')
print(check_point) 