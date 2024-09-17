'cat'                   # Yes
(3, 1, 4, 1, 5, 9, 2)   # Yes
['a', 'b']              # No - list is mutable
{'a': 1, 'b': 2}        # No - a dict
range(5)                # Yes
{1, 4, 9, 16, 25}       # No - set is mutable
3                       # Yes
0.0                      # Yes
frozenset({1, 4, 9, 16, 25}) # Yes