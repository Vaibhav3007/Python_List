my_list = [["Dog",3],["Apple",2],["Ball",4],["Egg",5],["Cat",1]]
my_list1 = my_list[:]
my_list1.sort()
print("Original list-",my_list)
print("Default sort-",my_list1)
my_list_sort = my_list[:]

for j in range(0,len(my_list_sort)):
    swap = 0
    for i in range(0,len(my_list_sort)-1):
        if my_list_sort[i][1] > my_list_sort[i+1][1]:
            temp = my_list_sort[i]
            my_list_sort[i] = my_list_sort[i+1]
            my_list_sort[i+1] = temp
            swap += 1

    if swap == 0:
        break



print("Sub-List sort-",my_list_sort)
