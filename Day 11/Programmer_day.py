year=int(input('year: '))
result=''
if year in range(1700,1918):
    if year % 4==0:
        print(f'12.09.{year}')
    else:
        print(f'13.09.{year}')
elif year in range(1919,2701):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result=8
            else:
                result=9
        else:
            result=8
    else:
        result=9
    
    if result==8:
        print(f'12.09.{year}')
    else:
        print(f'13.09.{year}')
elif year==1918:
    print(f'26.09.{year}')
