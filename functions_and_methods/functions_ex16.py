def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

#functions
# multiply (line 1, 9)
# get_num(line 4, 7, 8)
# float (line 5)
# input (line 5)
# print (line 10)

#parameters
# left & right (line 1, 2)
# prompt (line 4, 5),