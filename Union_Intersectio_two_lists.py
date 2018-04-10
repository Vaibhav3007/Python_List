a = [1,2,"name",4.0,5,[1,2],"a",["A","B"]]
b = [1,2,"name",3.0,5,[1,3],"A",["A","B"]]
c = []
for i in range(0,len(a)):
    if a[i] == b[i]:
        c.append(a[i])
        
print(a)
print(b)
print("Union of two lists",a+b)
print("Intersection of two lists",c)
