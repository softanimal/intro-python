my_list = [6, 3, 0, 11, 20, 4, 17]

# Print all the even numbers in the list
index = 0
while index < len(my_list):
    if index % 2 == 0:
        print(my_list[index])
    index += 1

# Print all the odd numbers in the list
for number in my_list:
    if number % 2 != 0:
        print(number)
