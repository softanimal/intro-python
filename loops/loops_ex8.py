my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = { pet: len(pet)
            for pet in my_set if len(pet) % 2 != 0 }

print(result)