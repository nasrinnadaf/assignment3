lenght_number = int(input("enter lenght of list :"))
list1 = []
sort_list = []
for i in range (0 , lenght_number):
   
    x = int(input("enter your numb: "))
list1.append(x)
sort_list.append(x)
sort_list.sort()
if list1 == sort_list :
    print("your list is sorted. ")
else :
    print(" your list is not sorted! ")