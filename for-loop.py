"""
syntax =>
for <variable> in <set/list/range> :
        <statement>

in keyword => check every element of list or range

range => range ( start_point , end_point , step )

"""

# print 1 to 10 numbers
for i in range(1, 11):
    print(i, end="\t")

print()
# print 10 to 1 in reverse form
for i in range(10, 0, -1):
    print(i, end="\t")

print()
# print odd values between 1 to 20
for i in range(1, 20, 2):
    print(i, end="\t")

print("\n")

# using loop in list
list1 = [1, 4, 64, 23, 52, 22]

for item in list1:
    print(item, end="\t")

print("\n")

# using loop in dictionary
dict1 = {"name": "jack", "age": 18, "marks": 82.42}

# print keys of dictionary
for item in dict1:
    print(item)
print()
# .items() function is required for accessing items stored in dictionary
for item, value in dict1.items():
    print(item, "is", value)
