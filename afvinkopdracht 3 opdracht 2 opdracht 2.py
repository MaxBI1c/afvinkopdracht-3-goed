lengthrectangle_one = int(input('What is the length of the first rectangle?'))
widthrectangle_one = int(input('What is the width of the first rectangle?'))
lengthrectangle_two = int(input('What is the length of the second rectangle?'))
widthrectangle_two = int(input('What is the width of the second rectangle?'))

area_rectangle_one = lengthrectangle_one * widthrectangle_one

area_rectangle_two = lengthrectangle_two * widthrectangle_two

if area_rectangle_one > area_rectangle_two :
    print('The first rectangle has a bigger area than the second rectangle')
elif area_rectangle_two < area_rectangle_one :
    print('The second rectangle has a bigger area than the first rectangle')
else:
    print('Both rectangles have the same area')
    
