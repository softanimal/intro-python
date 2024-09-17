# This was my first attempt at augmented assignment
balance = 1000
interest1 = balance * .05
total1 = int(interest1 + balance)
interest2 = total1 * .05
total2 = int(interest2 + total1)
interest3 = total2 * .05
total3 = int(total2 + interest3)
interest4 = total3 * .05
total4 = int(total3 + interest4)
interest5 = total4 * .05
total5 = int(total4 + interest5)

print(f'Your starting balance is ${balance}.')
print(f'After 1 year, you will have earned ${total1} with a 5% interest rate.')
print(f'After 2 year, you will have earned ${total2} with a 5% interest rate.')
print(f'After 3 year, you will have earned ${total3} with a 5% interest rate.')
print(f'After 4 year, you will have earned ${total4} with a 5% interest rate.')
print(f'After 5 year, you will have earned ${total5} with a 5% interest rate.')

# This was the provided solution code

balance = 1000.00
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)