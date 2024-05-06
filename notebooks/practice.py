def subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = 0
    for i in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += i
        max_sum = max(max_sum,current_sum)
    return max_sum

array_list = [-1,2,-3,5,6,-4]
print(f'Largest sum in an array is {subarray(array_list)}')