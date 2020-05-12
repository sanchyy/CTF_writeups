#!/usr/bin/env python

code = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

init = 65 - 1  # 'A' position in ascii table

for elem in code:
    if type(elem) == int:
        print(chr(init+elem), end='')
    else:
        print(elem, end='')
print()
