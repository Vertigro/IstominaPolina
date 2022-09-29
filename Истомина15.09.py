#x = int(1)
#y = int(1)
#z = int(1)
p = int(input("Введите р (2<p<=10):"))
for x in range(1, p):
    for y in range(1, p):
        z= (x*y//p)*10 + (x*y)%p
        print (z, end = ' ')
    print()
