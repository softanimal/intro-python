def num_range(n):
    if n < 0:
        print(f'{n} is less than 0.')
    elif n <= 50:
        print(f'{n} is between 0 and 50.')
    elif n <= 100:
        print(f'{n} is between 51 and 100.')
    else:
        print(f'{n} is greater than 100.')


num_range(0)
num_range(51)
num_range(101)
num_range(-50)