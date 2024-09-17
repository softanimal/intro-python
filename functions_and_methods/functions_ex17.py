def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# function names: say

# built-in functions: print, input, max

# method names: .upper(), lower()
