nums = [3, 5, 2, 10, 8, 6, 1, 4, 7, 9]

correct_nums = []

print(nums)

while nums:
    smallest = nums[0]
    
    for num in nums:
        if num < smallest:
            smallest = num

    correct_nums.append(smallest)
    nums.remove(smallest)

print(correct_nums)