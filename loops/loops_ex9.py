# def factorial(n):
#     result = 1
#     for number in range(n, 0, -1):
#         result *= number
    
#     return result


def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number

    return result

print(factorial(5))