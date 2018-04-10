n = int(input("Enter number of elements: "))
l1 = []
for i in range(1,n+1):
    l1.append((i,i**2,i**3))
print(l1)


l2 = ["Vaibhav","Rai","Python","coding","!"]
print(l2)
l2.sort(key = len)
print(l2)
