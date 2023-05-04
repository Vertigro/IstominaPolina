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
def f(a): #Рекурсия
    if a == 0: return 1
    return f(a - 1)
print(f(5))
s = [1, 2, 7, 4, 5, 6] #Поиск максисума или убить дракона
e = 0
for i in range(len(s)):
    si = s[i]
    if si >= e:
        e = si
print(e)

a = 123
print(a+a)
a = str(a)
print(a+a)

a = [x for x in range(101)] #5. Метод итераций или измерение на равноудаленных промежутках (доделать)
b = [x for x in range(51)]
b.reverse
a = a + b
print(a)
for i in range(len(a)):
    


t1 = [2, 4, 5, 8]  #Если верен каждый или если где-то плохо, то все плохо (доделать)
t = [2, 4, 6, 8]
if all t[i]%2 == 0:
   for i in range(len(t)):
       print('список четный')


        

