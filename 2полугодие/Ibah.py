s = []
for i in range(10, 20):
    a = str(i)
    b = int(len(a))
    f = list(a)
    print(f)
    for n in range(b):
        s = s + (f.pop(n))**b
        print(s)

    
   
        
    
