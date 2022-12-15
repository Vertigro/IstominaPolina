def f(): #Перевод из 10 системы счисления
    N10 = int(input("Введите исходное 10-чное число"))
    p = int(input("Введите основание системы"))
    k = int(1)
    Np=int(0)
    while N10 !=0:
        Np = Np + (N10%p)*k
        k = k*10
        N10 = N10//p
    print (f'N{p} = {Np}')
def g(): #Азбука Морзе
    a = 'A B W G D E V Z I J K L M N O P R S T U F H C Q X'
    abc=a.split(" ")
    print (abc)
    b = '.- -.. .-- --. -.. . ...- --.. .. .--- -.- .-.. -- - --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-'
    print (b)
    abcm = b.split()
    print (abcm)
    inda = ""
    text = input('введите текст для  перевода ')
    for i in range(len(text)):
        ind=abc.index(text[i])
        inda = inda + abcm[ind]   
    print(inda)
    
def y(): #Таблица умножения
    p=int()
    p=int(input(f"{p}-ичная таблица умножения"))
    for x in range(1,p):
        for y in range(1,p):
            z=(x*y//p)*10+(x*y)%p
            print(z,end=' ')
        print()
def b(): #код Хэмминга
    a='0123456789'
    nums=list(a)
    print(nums)
         

    b='0000000 0001111 0010110 0011001 000101 0101010 0110011 0111100 1000011 1001100'
    hem=b.split()
    print(hem)
    for i in range(len(hem)):
      hem[i]=int(hem[i])
    print(hem)
         

    def distance(x,y):
      k=7
      for i in range(7):
        if x%10==y%10:
          k=k-1
        x=x//10
        y=y//10
      return k
         

    cod=int(input("код"))
         

    cod=int(input("код"))
    min=distance(cod,hem[0])
    imin=0
    for i in range(10):
      D=distance(cod,hem[i])
      if D:

        if min==0:
            print(f"код верный: символ {nums[imin]}")
        elif min==1:
           print(f"код исправлен: символ {nums[imin]}")
        else:print("Код неверный")
            #print (i)

def p(): #Перевод из системы счисления в 10
    p = int(input('Введите основание СС исходного числа: p = '))
    valid = False
    while valid == False:
        Np = (input(f'Введите исходное число: N{p} = '))
        for i in range(1, len(Np)):
            if int(Np[i]) >= p:
                print('Недопустимое число!')
                valid = False
                break
            else:
                valid = True
                Np = int(Np)
    k = int(1)
    N10 = int(0)
    while not Np == 0:
        N10 = N10+(Np%10)*k
        k = k*p
        Np = Np//10
    print(f'N10 = {N10}')
p()
y()
f()
g()
b()
