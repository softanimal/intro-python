def all_caps(str):
    if len(str) > 10:
        return str.upper()
    else:
        return str
    
print(all_caps('Summer time is my favorite season.'))