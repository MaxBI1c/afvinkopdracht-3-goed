x = input('Reboot the computer,Did that fix the problem (yes or no)')

if x =='yes':
    print('mooi')
else:
    x = input('Reboot the router,Did that fix the problem?(yes or no)')
    if x =='yes':
        print('mooi')
    else:
        x = input('Are the cables plugged in,Did that fix the problem?(yes or no)')
        if x == 'yes':
            print('mooi')
        else:
            x = input('Move the router to a new location,Did that fix the problem?(yes or no)')
            if x =='yes':
                print('mooi')
            else:
                print('Get a new router')
