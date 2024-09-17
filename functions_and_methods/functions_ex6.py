# Does not print anything due to return before print call
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yippeee')