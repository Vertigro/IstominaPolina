a = ['1.Кто является даэдрическим принцем безумия в серии TES ','2.Как звали жену главного героя игры Castlevania: Lords of Shadow', '3.Кто из играбельных персонажей Dragon age Inqusition ранее служил в армии Орлея', '4.В каком городе была рвсположенна компания, в которой работал главный герой Fallout: New Vegas', '5.Как звали архонта Тайн в Tyranny']
b = ['Шеогорат', 'Мария', 'Блэкволл', 'Примм', 'Голоса Нерата']
right = int()
fols = int()
print (a)
for i in range(len(a)):
    print (a[i])
    print('Ваш ответ:')
    v = str(input())
    v1 = str(b[i])
    if v1 == v:
            print('Правильно')
            right = right + 1
    else:
        print('Неверно')
        fols = fols + 1
print ('Правильных ответов:', right, 'Неправильных ответов:', fols)
    