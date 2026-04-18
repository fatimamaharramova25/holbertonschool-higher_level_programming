#!/usr/bin/python3
def no_c(my_string):
    # 'c' və 'C' hərflərini boşluqla əvəz edirik (silirik)
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
