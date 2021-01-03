#!python3

# List items are ordered, changeable, and allow duplicate values.
# You can modify a list, adding and removing items
someList = ["Bob", "Rolf", "Anne"]

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
