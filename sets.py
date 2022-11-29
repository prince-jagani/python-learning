"""
set is same as sets in maths as a datatype in python

we can convert a list to set or can directly assign a set

syntax===>
s1 = set()

list = [ , , ]
s2 = set(list)

**here s1 and s2 are sets
** s1 is empty and s2 is set made with elements of list

characteristic of set datatype is also same with maths rules.
"""

set1 = set()
print(set1)

set1.add(1)
set1.add(5)
set1.add(3)
set1.add(1)  # one is already in set, so it will not store again

# set will be arranged in increasing order automatically
print(set1)

list1 = [1, 4, 2, 6, 2, 24, 6, 3, 2]
set2 = set(list1)
print(set2)

# set functions
print("Maximum:", max(set2))
print("Minimum:", min(set2))
print("Length:", len(set2))

# union and intersection of set
print(set2.union(set1))
print(set2.intersection(set1))

# check disjoint sets
print(set1.isdisjoint(set2))

# check subset and superset
set2.add(5)
print()
print(set1.issubset(set2))
print(set1.issuperset(set2))

print(set2.issubset(set1))
print(set2.issuperset(set1))
