"""
string slicing is used to divide string in parts
it is done with the [ ]

syntax =  string name[ starting point : ending point : steps ]

by default = string name[ 0 : length of string : 1 ]

**if you put str[::] it will get by default
**leaving any of argument in [] will also take that argument by default
"""

_str = "This is the string to Slice"
_str2skip = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# print original string
print(_str)
_len = len(_str)
print("Length=", _len)  # length of str

# [ 0 : length : 1 ]
print(_str[::])

# [ 0 : length : 1 ]
print(_str[0:_len:1])

# [ 0 : length : 1 ]
print(_str[0:_len])

# if over ranged then it will return output which are possible to return
print(_str[0:100])

# printing all words separately
print(_str[0:4], _str[5:7], _str[8:11], _str[12:18], _str[19:21], _str[22:27])

# negative index string
# in python strings have negative index from end of string starting -1 to the left side increasing
print()
print("String with one char skipped:", _str2skip[::2])
print("Reverse String:", _str2skip[::-1])
print("Reverse String:", _str2skip[-len(_str2skip):-1])  # skip last character

# string functions
print()
print("Lowercase:\t\t", _str2skip.lower())
print("Capitalize:\t\t", _str2skip.capitalize())
print("Is Alphabets:\t", _str2skip.isalpha())
print("Is lowercase:\t", _str2skip.islower())
print("Find:\t\t\t", _str2skip.find("CD"))
print("Replace:\t\t", (_str2skip.replace("ABC", "123")))
