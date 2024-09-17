#foo is not accessible to the global scope
def set_foo():
    foo = 'bar'

set_foo()
print(foo)