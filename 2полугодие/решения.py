def f5():
    for N in range(516):
        b = f'{N:b}'
        if N % 2 == 0: 
            b +='10'
        else:
            b = '1' + b + '01'
        if int(b, 2) > 516:
            print (N)
            break 
def f6():
        from turtle import *
    left(90)
    for i in range(7):
        forward(300)
        right(120)
    pu()
    for x in range(1,9):
        for y in range(1,10):
            goto(x*30,y*30)
            dot(5)
    done()
def f81():
    count = 0
    from itertools import product
    from a, b, c, d, e, in product(range(1,8), range(8), range(8), range(8), range(8)):
        s=str(a)+str(b)+str(c)+str(d)+str(e)
        if s.count('6')==1 and s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0: count+=1
        if s.count('6')==1 and s.index('6')==0 and int(s[1])%2==0: count+=1
        if s.count('6')==1 and s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
            count+=1
    print(count)
    
def f82():  
        from itertools import product
    nums=product('01234567',repeat=5)
    k=0
    n='16 36 56 76 61 63 65 67'
    nn=n.split()
    for n in nums:
        numb=''.join(n)
        sp=[]
        if numb.count('6')==1 and numb[0]!='0':
            for x in nn:
                if x in numb:
                    sp.append(x)
            if not sp: 
                k+=1
    print(k)
    
def f12():
        sp=[ ]
    for i in range(2,1000):
        n=0
        for y in range(2,i):
             if i%y ==0:
                 n += 1
        if n==0:
            sp.append(i)
    print (sp)
    for i in sp:
        for y in range (100):
            if y*4+105==i:
                print(y)

