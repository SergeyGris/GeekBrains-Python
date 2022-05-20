list_1=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2=['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
lists=[list_1,list_2]
for lst in lists:
    len_list = len(lst)
    i=0
    print("Исходный список:", '\n',lst,'\n')
    while i!=len_list: # я не знал как сделать этот цикл, поэтому методом тыка +i//3 =)
        if lst[i].isdigit()==True:
            lst[i]=lst[i].zfill(2)
            lst.insert(i,'"')
            lst.insert(i+2,'"')
            i+=3
        if '-'in lst[i] or '+'in lst[i]:
            lst[i] = lst[i].zfill(3)
            lst.insert(i, '"')
            lst.insert(i + 2, '"')
            i += 3
        len_list = len(lst)
        i+=1
    for x in range(len_list):
        if lst[x].isdigit()== True:
            list_str =''.join(lst)
        else:
            list_str =' '.join(lst)
#        list_str=list_str.replace(' " ','"')
    print('Новый список + добавление элементов-кавычек:','\n',lst,'\n','\n','Строка:','\n', list_str,'\n','\n','\n','====================================================')

