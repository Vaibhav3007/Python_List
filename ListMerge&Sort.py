#List merging and sorting

import random

list1 = []
list2 = []

for i in range(0,5):
    list1.append(random.randrange(500,2501))

for i in range(0,7):
    list2.append(random.randrange(500,2501))

print(list1)
print(list2)

list3 = list1+list2

list3.sort()
print(list3)
