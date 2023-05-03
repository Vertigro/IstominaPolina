from itertools import product
a = [x for x in range(4)]
for i in a: #перебор списка способ 1
    print(i)
for i in range(len(a)): #перебор списка способ 2
    print(a[i])
for x in range(len(a)):
    for y in range(len(a)):
        print(a[x],a[y])
for x in range(len(a)):
    for y in range(x+1, len(a)):
        print(a[x],a[y])
b = list(product('012',repeat=2))
print(b) 

