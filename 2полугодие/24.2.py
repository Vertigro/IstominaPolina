with open('24.txt') as f:
    S = f.readline().replace('C','S').replace('D','S').replace('F','S')
    S = S.replace('A','6').replace('O','6')
    S = S.replace('S6','*')
    kmax = 0
    cnt = 0
    for i in range(len(S)):
        if S[i] == '*':
            cnt = cnt +1
            kmax = max(kmax,cnt)
        else:
            cnt = 0
print(kmax)
    
