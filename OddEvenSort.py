#Odd-Even sorting

import random

nums = []

for i in range(0,10):
    nums.append(random.randrange(500,2501))

odd = [nums[x] for x in range(len(nums)) if nums[x]%2 == 1]
even = [nums[x] for x in range(len(nums)) if nums[x]%2 == 0]

print("The List - ",nums)
print("Odd List - ",odd)
print("Even List - ",even)
