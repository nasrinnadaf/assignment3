import random
len_snake =int(input("put number:  "))
for i in range (len_snake):
    if i %2 == 0:
        print("*" , end ='')
    else :
        print("#", end ='')