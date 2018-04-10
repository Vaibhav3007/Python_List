#Largest number in a list


import random

a = []

for i in range(0,4):
    a.append(random.randrange(-100,101))

n = len(a)
temp = 0
print(a)
for count in range(0,n):
    swap = 0
    print("Step-",count+1)
    
    for i in range(0,n-1):
        print("Iteration-",i+1,"of step-",count+1)
        
        if a[i]>a[i+1]:
            temp = a[i]
            a[i]=a[i+1]
            a[i+1]=temp
            print(a,"Swap Done")
            swap = swap + 1
        else:
            print("No Swap done")
    
    print("List after completion of step-",count+1,a)
    print("Number of swaps done-",swap)
    print()
    if swap == 0:
        break

print("Final-",a)
print("Second largest element:",a[-2])
