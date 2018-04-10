#Largest number in a list


import random

nums = []

for i in range(0,11):
    nums.append(random.randrange(500,2501))

print(nums)

max_num = 0
for j in nums:
    if j > max_num:
        max_num = j

print(max_num)
