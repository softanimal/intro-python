my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Are the lists assigned to my_list and another_list equal?
    # Yes, they have the same elements and are both lists
# Are the lists assigned to my_list and another_list the same object?
    # No, copies of the elements were created
# Are the nested lists at index 3 of my_list and another_list equal?
    # Yes, they are the same elements
# Are the nested lists at index 3 of my_list and another_list the same object?
    # Yes, they are the same object due to shallow copy.