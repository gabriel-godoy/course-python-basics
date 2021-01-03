#!python3

nums = [1, 2, 3]

print('Type: ', type(nums))  # list

nums.append(3)
nums.append(4)
nums.append(5)

print('List length: ', len(nums))

nums[3] = 100

nums.insert(0, -200)

print('Last list item: ', nums[-1])
print('List: ', nums)
