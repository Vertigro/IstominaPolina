print('какой тип звдачь вы хотите решить:\n1 - кодирование информации\n2 - кодирование звука\n3 - кодирование изображения\n') 
n = input()
print(n)
if n == "1":
    print("Что вы хотите расчитать?:\n1 - разряд двоичного кода\n2 - мощность алфаовита (количество символов)")
    n1 = input()
    if n1 == "1":
        print('введите мощность алфаовита (количество символов)')
        N = input()
        i = 1
        while 2**i != (int(N)):
            i = i + 1
        print(i)
        
        print("введите переменную, которую нужно найти: i, N")
        k = input()
        print(k)
        if k == "i":
            print('введите N')
            N = input()
            i = 1
            while 2**i != (int(N)):
                i = i + 1
            print(i)
        else:
            print('ведите i')
            i = input(int())
            k2 = 2**(int(i))
            print(k2)
    else:
        print("введите переменную, которую нужно найти: i, K, I")
        m = input()
        if m == "i":
            print ('введите переменную K')
            K = input()
            print ('введите переменную I')
            I = input()
            i = int(I) // int(K)
            print(i)
        elif m == "I":
            print ('введите переменную K')
            K = input()
            print ('введите переменную i')
            i = input()
            I = int(i) * int(K)
            print(I)
        else:
            print ('введите переменную I')
            I = input()
            print ('введите переменную i')
            i = input()
            K = int(I) // int(i)
            print(K)
elif n == "2":
    print("Выбирете формулу, по которой вы хотите провести расчёт: 1 - (2**b = K),2 - (I=Htb)")
    n2 = input()
    if n2 == "1":
        print("введите переменную, которую нужно найти: b, K")
        k = input()
        print(k)
        if k == "b":
            print('введите K')
            K = input()
            b = 1
            while 2**b != (int(K)):
                b = b + 1
            print(b)
        else:
            print('ведите b')
            b = input(int())
            k2 = 2**(int(b))
            print(k2)
    else:
        print("введите переменную, которую нужно найти: I,t,b,H")
        h = input()
        if h == "I":
            print ('введите переменную t')
            t = input()
            print ('введите переменную b')
            b = input()
            print ('введите переменную H')
            H = input()
            I = int(H)*int(b)*int(t)
            print(I)
        elif h == "t":
            print ('введите переменную I')
            I = input()
            print ('введите переменную b')
            b = input()
            print ('введите переменную H')
            H = input()
            t = int(I)//(int(H)*int(b))
            print(t)
        elif h == "H":
            print ('введите переменную I')
            I = input()
            print ('введите переменную t')
            t = input()
            print ('введите переменную b')
            b = input()
            H = int(I)//(int(t)*int(b))
            print(H)
        elif h == "b":
            print ('введите переменную t')
            t = input()
            print ('введите переменную H')
            H = input()
            print ('введите переменную I')
            I = input()
            b = int(I)//(int(t)*int(H))
            print(b)
else:
    print("введите переменную, которую нужно найти: b, K")
    k = input()
    print(k)
    if k == "b":
        print('введите K')
        K = input()
        b = 1
        while 2**b != (int(K)):
            b = b + 1
        print(b)
    else:
        print('ведите b')
        b = input(int())
        k2 = 2**(int(b))
        print(k2)
     
    
    
    
