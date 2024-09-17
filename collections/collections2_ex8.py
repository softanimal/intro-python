# The first print aligns the 0 index starting at index 21
# The second print aligns the 0 index starting at the beginning of the string
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29