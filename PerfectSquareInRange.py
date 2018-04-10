s = int(input("Start of range- "))
e = int(input("End of range- "))

"""l1 = [x for x in range(s,e+1)]
l2 = []
for i in range(len(l1)):
    a = l1[i]**(1/2)
    if int(a)*int(a) == l1[i]:
        l2.append(l1[i])

print("perfect squares\n",l2)
"""


l3 = [y for y in range(s,e+1) if (int(y**0.5)**2)==y]
print(l3)
