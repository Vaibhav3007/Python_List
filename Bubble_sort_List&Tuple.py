A = [(1,2),(5,1),(0,9),(8,1),(0,0),(7,5),(4,2)]
B = A[:]
for i in range (0,len(A)):
    swap = 0
    for j in range(0,len(A)-1):
        if A[j][1] > A[j+1][1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
            swap += 1
    if swap == 0:
        break
print("Original List",B)            
print("Sorted List",A)
        
