# This code will raise an error due to missing third default value
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)