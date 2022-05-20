predel=int(input('Пожалуйста, введите предел от 1 до скольки посчитать сумму?'))
import math
number=1
total_sum=0
while number<=predel:
    cubic_number=number**3
    remain=cubic_number
    if number%2!=0:
        sum=0
        power=int(math.log10(cubic_number))
        while power>=0:
            new_number=remain//(10**power)
            remain=remain-new_number*(10**power)
            sum=sum+new_number
            power=power-1
        if sum%7==0:
            total_sum=total_sum+number
            print(str(number)+'^3: '+str(cubic_number)+' sum: '+str(total_sum)+' ['+str(sum)+']')
    number=number+1
