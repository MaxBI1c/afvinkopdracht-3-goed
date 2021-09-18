pocketnumber = int(input('Enter an pocketnumber'))


if pocketnumber >= 1 and pocketnumber <=10:
    if pocketnumber %2 ==0:
        print('Black')
    else:
        print('Red')
elif pocketnumber >=11 and pocketnumber <=18:
    if pocketnumber %2 ==0:
        print('Red')
    else:
        print('Black')
elif pocketnumber >=19 and pocketnumber <=28:
    if pocketnumber %2 ==0:
        print('Black')
    else:
        print('Red')
elif pocketnumber >=29 and pocketnumber <=36:
    if pocketnumber %2 ==0:
        print('Red')
    else:
        print('Black')
elif pocketnumber <0 or pocketnumber > 36:
    print('Please enter a smaller number')
else:
    print('Green')
