"""
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
lst_info = list(info)
lst_info[3] = '+'
lst_info[5] = '+'
lst_info[8] = '+'
lst_info[11] = '+'
lst_info[29] = '+'
print(lst_info())
"""

info = 'xyz:*:42:441:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts)
print(result)
