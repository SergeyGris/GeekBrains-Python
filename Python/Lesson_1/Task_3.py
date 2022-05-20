input_number=0
while input_number<=100:
    number=str(input_number)
    p='процент'
    if 5<=int(number)<=20:
        suffix='ов'
    elif 5<=int(number[-1])<=9 or 0==int(number[-1]):
        suffix='ов'
    elif 2<=int(number[-1])<=4:
        suffix='а'
    else:
        suffix=''
    print(number+' '+p+suffix)
    input_number=input_number+1