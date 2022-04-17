from operator import le
import random
araye = []
length_araye = int(input(" put length of araye :"))
while length_araye != len(araye) :

    x = random.randint (0,20) 
    if x not in araye:
        araye.append(x)
    print("araye :" , araye)