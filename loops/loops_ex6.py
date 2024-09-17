my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for number in my_list:
    if number % 2 == 0:
        number = 'even'
    else:   
        number = 'odd'
    new_list.append(number)

print(new_list)