with open('26.txt') as f:
    s = [int(x)  for x in f]
    s.pop(0)
    s.sort(reverse = True)
    m = s[0]
    k = 0
    for i in range(1,len(s)):
        if s[i] +3<= m:
            m = s[i]
            k = k +1
print(k,m)
