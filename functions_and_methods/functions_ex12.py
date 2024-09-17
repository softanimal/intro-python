# This code will raise an error due to missing 1st arguement
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()