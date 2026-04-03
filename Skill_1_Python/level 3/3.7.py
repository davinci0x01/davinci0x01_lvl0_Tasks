def remove_duplicates(input_list):
    correct_list = []
    for item in input_list:
        if item not in correct_list:
            correct_list.append(item)
    return correct_list

nums = [3, 5, 2, 10, 8, 6, 1, 4, 7, 9, 3, 5, 2]

print(nums)
print(remove_duplicates(nums))