age = input('How old are you? ')
print()

print(f'You are {age} years old.')

for decade in range(10, 50, 10):
    print(f'In {decade} years, you will be {int(age) + decade} '
          f'years old.')