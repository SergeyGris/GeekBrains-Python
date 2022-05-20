from copy import deepcopy
price=[57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]
print('Исходный список: ', '\n',price)
a=id(price)
price.sort()
price_2=deepcopy(price)
b=id(price)
for i in range(len(price)):
    rubles=int(price[i])
    penny=(price[i]-rubles)*100
    new_price="%02d руб %02d коп"%(rubles,penny)
    price[i]=new_price
print(",".join(price),'\n',
    'Доказательство операции in place:',
    '\n','id перед сортировкой ',a,
    '\n','id после  сортировки',b,
    '\n',price_2, #Только для того, чтобы вывести неотформатированный список
    '\n', '5 cамых дорогих товаров:'
)
price_2.reverse()
for i in range(len(price_2[:5])):
    print(price_2[i])