a = [1,1,"V","v",1,2,2,2,[1,2],"v",3,[1,2],[2,3],3,3]
b = []
c = []
for x in a:
    if x not in b:
        b.append(x)
    else:
        c.append(x)
        
print("Original List",a)
print("Edited List",b)
print("Copy Items",c)

