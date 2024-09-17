#print(foo) is accessing the global scope to print'bar'
foo = 'bar'
def set_foo():
    foo = 'qux'

set_foo()
print(foo)