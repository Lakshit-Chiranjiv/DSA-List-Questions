# print largest number by rearranging elements of list

def largest_number(nums):

    if len(nums) == 1:
        return str(nums[0])

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if int(str(nums[i])+str(nums[j])) < int(str(nums[j])+str(nums[i])):
                nums[i], nums[j] = nums[j], nums[i]
    return ''.join(map(str, nums))

nums = [3, 30, 34, 5, 9]
print(largest_number(nums))