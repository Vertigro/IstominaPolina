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
    
    

