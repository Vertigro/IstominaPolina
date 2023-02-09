cout = 0
c = 0
from itertools import product
for i in range(1, 10):
    b = product ('12',repeat = i)
    for n in b:
        a = 1
        for x in n:
            if x == '1':a +=1
            else:
                a = a * 2
        if a == 10:
            cout = 1 + cout
print(cout)
from itertools import product
for i in range(2, 25):
    d = product ('12',repeat = i)
    for k in d:
        l = 10
        for y in k:
            if y == '1':
                l +=1
            
            else:
                l = l * 2
            if l == 17:
                    break
        if l == 35:
            c = 1 + c 
print(cout * c)   
