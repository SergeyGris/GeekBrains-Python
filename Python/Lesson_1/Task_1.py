duration=input('Введите количество секунд')
seconds=int(duration)%86400%3600%60
hour=int(duration)%86400//3600
minute=int(duration)%86400%3600//60
day=int(duration)//86400
answer=str(seconds)+" сек"
if minute!=0:
    answer=str(minute)+" мин "+answer
elif minute==0 and hour!=0:
    answer = str(minute) + " мин " + answer
if hour!=0:
    answer=str(hour)+" час "+answer
elif hour==0 and day!=0:
    answer = str(hour) + " час " + answer
if day!=0:
    answer=str(day)+" дн "+answer
print(answer)
